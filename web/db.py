import sqlite3

import click
from flask import current_app, g

from simulation.simulation import Simulation


def get_db():
	if 'db' not in g:
		g.db = sqlite3.connect(
			current_app.config['DATABASE'],
			detect_types=sqlite3.PARSE_DECLTYPES
		)
		g.db.row_factory = sqlite3.Row
	
	return g.db


def close_db(e=None):
	db = g.pop('db', None)
	
	if db is not None:
		db.close()


def init_db():
	db = get_db()
	
	with current_app.open_resource('schema.sql') as f:
		db.executescript(f.read().decode('utf8'))


def populate_db():
	database = get_db()
	
	sim = Simulation()
	
	for key, simulation in sim.simulations.items():
		database.execute(
			'INSERT INTO simulations (key, value) VALUES (?, ?)', (key, simulation.value)
		)
		database.commit()
	
	for key, situation in sim.situations.items():
		database.execute(
			'INSERT INTO situations (key, is_active) VALUES (?, ?)', (key, situation.is_active)
		)
		database.commit()
		
	for key, policy in sim.policies.items():
		database.execute(
			'INSERT INTO policies (key, is_active, slider_value, value) VALUES (?, ?, ?, ?)',
			(key, policy.is_active, policy.slider_value, policy.value)
		)
		database.commit()
		
	for key, _ in sim.groups.items():
		database.execute(
			'INSERT INTO groups (key) VALUES (?)', (key, )
		)
		database.commit()


@click.command('init-db')
def init_db_command():
	"""Clear the existing data and create new tables."""
	init_db()
	populate_db()
	click.echo('Initialized and populated the database.')


def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)


def simulation_from_database() -> Simulation:
	database = get_db()
	
	sim = Simulation()
	
	# populate simulations
	simulation_items = database.execute(
		'SELECT s.id, s.key, s.value FROM simulations AS s'
	).fetchall()
	
	for simulation_item in simulation_items:
		sim.simulations[simulation_item['key']].value = simulation_item['value']
		
		# handle loading historic simulation values
		simulation_histories_items = database.execute(
			'SELECT s.value FROM simulation_histories AS s WHERE simulation_id = ?', (simulation_item['id'], )
		).fetchall()
		
		for simulation_histories_item in simulation_histories_items:
			sim.simulations[simulation_item['key']].history.append(simulation_histories_item["value"])
	
	# populate situations
	situation_items = database.execute(
		'SELECT s.id, s.key, s.is_active FROM situations AS s'
	).fetchall()
	
	for situation_item in situation_items:
		situation_key = situation_item['key']
		situation_id = situation_item['id']
		sim.situations[situation_key].is_active = situation_item['is_active']
		
		# handle loading historic situation values
		situation_histories_items = database.execute(
			'SELECT s.value FROM situation_histories AS s WHERE situation_id = ?', (situation_id,)
		).fetchall()
		
		for situation_histories_item in situation_histories_items:
			history_value = situation_histories_item["value"]
			sim.situations[situation_key].history.append(history_value)
	
	# populate policies
	policy_items = database.execute(
		'SELECT p.id, p.key, p.is_active, p.slider_value, p.value FROM policies AS p'
	).fetchall()
	
	for policy_item in policy_items:
		policy_key = policy_item['key']
		policy_id = policy_item['id']
		sim.policies[policy_key].is_active = policy_item['is_active']
		sim.policies[policy_key].slider_value = policy_item['slider_value']
		sim.policies[policy_key].value = policy_item['value']
		
		# handle loading historic policy values
		policy_histories_items = database.execute(
			'SELECT s.value FROM policy_histories AS s WHERE policy_id = ?', (policy_id,)
		).fetchall()
		
		for policy_histories_item in policy_histories_items:
			history_value = policy_histories_item["value"]
			sim.policies[policy_key].history.append(history_value)
		
	# populate groups
	group_items = database.execute(
		'SELECT g.id, g.key FROM groups AS g'
	).fetchall()
	
	for group_item in group_items:
		group_key = group_item['key']
		group_id = group_item['id']
		
		# handle loading historic policy values
		group_histories_items = database.execute(
			'SELECT g.mood_value, g.freq_value FROM group_histories AS g WHERE g.group_id = ?', (group_id,)
		).fetchall()
		
		for policy_histories_item in group_histories_items:
			history_mood_value = policy_histories_item["mood_value"]
			history_freq_value = policy_histories_item["freq_value"]
			sim.groups[group_key].mood.history.append(history_mood_value)
			sim.groups[group_key].freq.history.append(history_freq_value)
	
	return sim


def simulation_to_database(sim: Simulation):
	database = get_db()
	
	# simulations
	for key, simulation in sim.simulations.items():
		database.execute(
			'UPDATE simulations SET value = ? WHERE key = ?',
			(simulation.value, key)
		)
		database.commit()
		
		# print(f'key={key}')
		simulation_row = database.execute(
			'SELECT s.id FROM simulations AS s WHERE key = ?',
			(key,)
		).fetchone()
		if simulation_row is None:
			raise Exception(f'cant find simulation "{key}" in db')
		
		simulation_id = simulation_row[0]
		
		database.execute(
			'DELETE FROM simulation_histories WHERE simulation_id = ?',
			(simulation_id,)
		)
		database.commit()
		
		for simulation_history_value in simulation.history:
			database.execute(
				'INSERT INTO simulation_histories (simulation_id, value) VALUES (?, ?)',
				(simulation_id, simulation_history_value)
			)
			database.commit()
	
	# situations
	for key, situation in sim.situations.items():
		database.execute(
			'UPDATE situations SET is_active = ? WHERE key = ?',
			(situation.is_active, key)
		)
		database.commit()
		
		situation_row = database.execute(
			'SELECT s.id FROM situations AS s WHERE key = ?',
			(key,)
		).fetchone()
		situation_id = situation_row[0]
	
		database.execute(
			'DELETE FROM situation_histories WHERE situation_id = ?',
			(situation_id,)
		)
		database.commit()
	
		for situation_history_value in situation.history:
			database.execute(
				'INSERT INTO situation_histories (situation_id, value) VALUES (?, ?)',
				(situation_id, situation_history_value)
			)
			database.commit()

	# polices
	for key, policy in sim.policies.items():
		database.execute(
			'UPDATE policies SET is_active = ?, slider_value = ?, value = ? WHERE key = ?',
			(policy.is_active, policy.slider_value, policy.value, key)
		)
		database.commit()
		
		policy_row = database.execute(
			'SELECT p.id FROM policies AS p WHERE key = ?',
			(key,)
		).fetchone()
		if policy_row is None:
			raise Exception(f'cant find policy "{key}" in db')
		
		policy_id = policy_row[0]
		
		database.execute(
			'DELETE FROM policy_histories WHERE policy_id = ?',
			(policy_id,)
		)
		database.commit()
		
		for policy_history_value in policy.history:
			database.execute(
				'INSERT INTO policy_histories (policy_id, value) VALUES (?, ?)',
				(policy_id, policy_history_value)
			)
			database.commit()
		
	# groups
	for key, group in sim.groups.items():
		
		group_row = database.execute(
			'SELECT g.id FROM groups AS g WHERE g.key = ?', (key,)
		).fetchone()
		if group_row is None:
			raise Exception(f'cant find group "{key}" in db')
		
		group_id = group_row[0]
		
		database.execute(
			'DELETE FROM group_histories WHERE group_id = ?', (group_id,)
		)
		database.commit()
		
		for index in range(0, len(group.mood.history)):
			group_mood_history_value = group.mood.history[index]
			group_freq_history_value = group.mood.history[index]
			database.execute(
				'INSERT INTO group_histories (group_id, mood_value, freq_value) VALUES (?, ?, ?)',
				(group_id, group_mood_history_value, group_freq_history_value)
			)
			database.commit()
	
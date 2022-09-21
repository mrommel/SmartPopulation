import sqlite3
import click
from flask import current_app, g

from simulation.base import SimulationCategory, SimulationBase, SituationBase
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
	db = get_db()
	
	sim = Simulation()
	
	for key, simulation in sim.simulations.items():
		db.execute(
			'INSERT INTO simulations (key, value)'
			' VALUES (?, ?)',
			(key, simulation.value)
		)
		db.commit()
	
	for key, situation in sim.situations.items():
		db.execute(
			'INSERT INTO situations (key, is_active)'
			' VALUES (?, ?)',
			(key, situation.is_active)
		)
		db.commit()


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
		'SELECT '
		'  s.key, s.value '
		'FROM '
		'  simulations AS s'
	).fetchall()
	
	for simulation_item in simulation_items:
		sim.simulations[simulation_item['key']].value = simulation_item['value']
		print(f"updated: {simulation_item['key']} = {simulation_item['value']}")
	# @todo: handle loading historic simulation values
	
	# populate situations
	situation_items = database.execute(
		'SELECT '
		'  s.key, s.is_active '
		'FROM '
		'  situations AS s'
	).fetchall()
	
	for situation_item in situation_items:
		sim.situations[situation_item['key']].is_active = situation_item['is_active']
		print(f"updated: {situation_item['key']} = {situation_item['is_active']}")
	
	# @todo: handle loading historic simulation values
	
	return sim

import os

import pandas as pd
from flask import Flask, render_template, request

import json
import plotly
import plotly.express as px

from simulation.base import SimulationCategory
from web.db import get_db, simulation_from_database, simulation_to_database, init_db, populate_db


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)
	
	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)
	
	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	from . import db
	db.init_app(app)
	
	@app.route("/", methods=('GET', 'POST'))
	def index():
		if request.method == 'POST':
			action = request.form['action']
			if action == 'next_turn':
				sim = simulation_from_database()
				sim.iterate()
				simulation_to_database(sim)
			elif action == 'reset':
				init_db()
				populate_db()
				sim = simulation_from_database()
			else:
				print(f'unknown action: {action}')
				sim = simulation_from_database()
		else:
			sim = simulation_from_database()
		
		return render_template('index.html', simulation_count=len(sim.simulations))
	
	@app.route("/simulations")
	def simulations():
		sim = simulation_from_database()
		
		# enrich simulations
		for key, simulation_item in sim.simulations.items():
			if simulation_item.value > 0.8:
				simulation_item.prop = 'bg-success'
			elif simulation_item.value > 0.6:
				simulation_item.prop = 'bg-primary'
			elif simulation_item.value > 0.4:
				simulation_item.prop = 'bg-warning'
			elif simulation_item.value > 0.2:
				simulation_item.prop = 'bg-orange'
			else:
				simulation_item.prop = 'bg-danger'
		
		return render_template('simulations.html', simulations=sim.simulations)
	
	@app.route('/simulation_callback', methods=[' POST', 'GET'])
	def cb():
		# request.args.get('data')
		return simulation_history('key')
	
	@app.route('/simulation/<key>')
	def simulation(key):
		sim = simulation_from_database()
		
		simulation_item = sim.simulations[key]
		
		# enrich the simulation
		if simulation_item.value > 0.8:
			simulation_item.prop = 'bg-success'
		elif simulation_item.value > 0.6:
			simulation_item.prop = 'bg-primary'
		elif simulation_item.value > 0.4:
			simulation_item.prop = 'bg-warning'
		elif simulation_item.value > 0.2:
			simulation_item.prop = 'bg-orange'
		else:
			simulation_item.prop = 'bg-danger'
			
		simulation_item.input_list = simulation_item.input_values(sim)
		simulation_item.effect_list = simulation_item.effect_values(sim)
		
		return render_template('simulation.html', simulation=simulation_item, graph_json=simulation_history(key))
	
	def simulation_history(key):
		sim = simulation_from_database()
		
		simulation_item = sim.simulations[key]
		
		data = simulation_item.history # list(reversed(simulation_item.history))
		d = {"iteration": range(0, len(data)), "history": data}
		df = pd.DataFrame(d)
		
		fig = px.line(df, title="History", x="iteration", y="history", range_y=[0.0, 1.0], template="plotly_dark")
		graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
		return graph_json
	
	@app.route("/groups")
	def groups():
		sim = simulation_from_database()
		
		# enrich simulations
		for key, group_item in sim.groups.items():
			if group_item.mood.value > 0.8:
				group_item.mood_prop = 'bg-success'
			elif group_item.mood.value > 0.6:
				group_item.mood_prop = 'bg-primary'
			elif group_item.mood.value > 0.4:
				group_item.mood_prop = 'bg-warning'
			elif group_item.mood.value > 0.2:
				group_item.mood_prop = 'bg-orange'
			else:
				group_item.mood_prop = 'bg-danger'
			
			if group_item.freq.value > 0.8:
				group_item.freq_prop = 'bg-success'
			elif group_item.freq.value > 0.6:
				group_item.freq_prop = 'bg-primary'
			elif group_item.freq.value > 0.4:
				group_item.freq_prop = 'bg-warning'
			elif group_item.freq.value > 0.2:
				group_item.freq_prop = 'bg-orange'
			else:
				group_item.freq_prop = 'bg-danger'
		
		return render_template('groups.html', groups=sim.groups)
	
	@app.route("/group/<key>")
	def group(key):
		sim = simulation_from_database()
		
		group_item = sim.groups[key]
		
		if group_item.mood.value > 0.8:
			group_item.mood_prop = 'bg-success'
		elif group_item.mood.value > 0.6:
			group_item.mood_prop = 'bg-primary'
		elif group_item.mood.value > 0.4:
			group_item.mood_prop = 'bg-warning'
		elif group_item.mood.value > 0.2:
			group_item.mood_prop = 'bg-orange'
		else:
			group_item.mood_prop = 'bg-danger'
		
		if group_item.freq.value > 0.8:
			group_item.freq_prop = 'bg-success'
		elif group_item.freq.value > 0.6:
			group_item.freq_prop = 'bg-primary'
		elif group_item.freq.value > 0.4:
			group_item.freq_prop = 'bg-warning'
		elif group_item.freq.value > 0.2:
			group_item.freq_prop = 'bg-orange'
		else:
			group_item.freq_prop = 'bg-danger'
		
		group_item.mood.input_list = group_item.mood.input_values(sim)
		group_item.freq.input_list = group_item.freq.input_values(sim)
		
		return render_template('group.html', group=group_item)
	
	@app.route("/situations")
	def situations():
		sim = simulation_from_database()
		
		# enrich simulations
		for key, situation_item in sim.situations.items():
			if situation_item.is_active:
				situation_item.prop = 'bg-success'
			else:
				situation_item.prop = 'bg-danger'
		
		return render_template('situations.html', situations=sim.situations)
	
	@app.route('/situation/<key>')
	def situation(key):
		sim = simulation_from_database()
		
		situation_item = sim.situations[key]
		
		# enrich the simulation
		if situation_item.is_active:
			situation_item.prop = 'bg-success'
		else:
			situation_item.prop = 'bg-danger'
			
		situation_item.input_list = situation_item.input_values(sim)
		situation_item.effect_list = situation_item.effect_values(sim)
		
		return render_template('situation.html', situation=situation_item, graph_json=situation_history(key))
	
	def situation_history(key):
		sim = simulation_from_database()
		
		situation_item = sim.situations[key]
		
		data = situation_item.history  # list(reversed(simulation_item.history))
		d = {
			'iteration': range(0, len(data)),
			'history': data,
			'start': [situation_item.start_trigger] * len(data),
			'end': [situation_item.end_trigger] * len(data)
		}
		df = pd.DataFrame(d)
		
		fig = px.line(df, title='History', x='iteration', y=['history', 'start', 'end'], range_y=[0.0, 1.0], template="plotly_dark")
		graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
		return graph_json
	
	@app.route("/policies")
	def policies():
		sim = simulation_from_database()
		
		return render_template('policies.html', policies=sim.policies)
	
	@app.route('/policy/<key>', methods=('GET', 'POST'))
	def policy(key):
		if request.method == 'POST':
			action = request.form['action']
			slider_value = request.form['slider']
			
			if action == 'change':
				sim = simulation_from_database()
				
				policy_item = sim.policies[key]
				policy_item.slider_value = slider_value
				
				# determine value
				step_value = 1.0 / len(policy_item.slider)
				
				try:
					slider_index = policy_item.slider.index(slider_value)
					policy_item.value = step_value * (slider_index + 1.0)
					print(f'Update policy "{key}" to {policy_item.value} / index: {slider_index} / {slider_value}')
				except ValueError:
					print(f'Could not find {slider_value} in {policy_item.slider}')
				
				simulation_to_database(sim)
			else:
				print(f'unknown action: {action}')
				sim = simulation_from_database()
		else:
			sim = simulation_from_database()
		
		policy_item = sim.policies[key]
		
		# situation_item.input_list = situation_item.input_values(sim)
		policy_item.effect_list = policy_item.effect_values(sim)
		
		return render_template('policy.html', policy=policy_item)
	
	@app.route("/categories")
	def categories():
		category_items = SimulationCategory
		
		return render_template('categories.html', categories=category_items)
	
	@app.route('/category/<key>')
	def category(key):
		sim = simulation_from_database()
		category_item = SimulationCategory[key]
		
		# {k: v for k, v in points.items() if v[0] < 5 and v[1] < 5}
		category_item.simulations = {k: simulation_item for k, simulation_item in sim.simulations.items() if
		                             simulation_item.category.value == category_item.value}
		category.situations = []
		category.policies = []
		
		return render_template('category.html', category=category_item)
	
	return app

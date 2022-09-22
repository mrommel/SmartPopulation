import os

from flask import Flask, render_template, request

from web.db import get_db, simulation_from_database, simulation_to_database


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
			simulation = simulation_from_database()
			simulation.iterate()
			simulation_to_database(simulation)
			
		database = get_db()
		simulation_count = database.execute(
			'SELECT count(*) as simulation_count FROM simulations'
		).fetchall()
		
		return render_template('index.html', simulation_count=simulation_count[0][0])
	
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
		
		return render_template('simulation.html', simulation=simulation_item)
	
	@app.route("/groups")
	def groups():
		return render_template('groups.html')
	
	@app.route("/situations")
	def situations():
		return render_template('situations.html')
	
	@app.route("/policies")
	def policies():
		return render_template('policies.html')
	
	return app

import os

from flask import Flask, render_template

from web.db import get_db


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
	
	@app.route("/")
	def index():
		db = get_db()
		simulation_count = db.execute(
			'SELECT count(*) as simulation_count FROM simulations'
		).fetchall()
		
		return render_template('index.html', simulation_count=simulation_count[0][0])
	
	@app.route("/dashboard")
	def dashboard():
		return render_template('dashboard.html')
	
	@app.route("/simulations")
	def simulations():
		db = get_db()
		simulation_items = db.execute(
			'SELECT '
			'  s.id, s.name, s.description, c.name as category_name, s.value, s.min_value, s.max_value '
			'FROM '
			'  simulations AS s'
			'  INNER JOIN categories AS c ON s.category_id = c.id'
		).fetchall()
		
		return render_template('simulations.html', simulations=simulation_items)
	
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

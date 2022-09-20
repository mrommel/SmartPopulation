from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')


@app.route("/dashboard")
def dashboard():
	return render_template('index.html')


@app.route("/simulations")
def simulations():
	return render_template('simulations.html')

@app.route("/groups")
def groups():
	return render_template('groups.html')


@app.route("/situations")
def situations():
	return render_template('situations.html')

"""General page routes."""
from flask import Blueprint, request
from flask import render_template

from web import simulation_from_database, simulation_to_database, init_db, populate_db

# Blueprint Configuration
home_blueprint = Blueprint(
    "home_blueprint", __name__, template_folder="templates", static_folder="static"
)


@home_blueprint.route("/", methods=('GET', 'POST'))
def index():
    """Homepage."""
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

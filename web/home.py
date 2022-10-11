"""General page routes."""
from flask import Blueprint, request, make_response
from flask import render_template

from . import db, global_simulation
from .models import Simulations, load_from_db, store_to_db

# Blueprint Configuration
home_blueprint = Blueprint(
    "home_blueprint", __name__, template_folder="templates", static_folder="static"
)


@home_blueprint.route("/", methods=['GET', 'POST'])
def index():
    """Homepage."""
    if request.method == 'POST':
        action = request.form['action']
        if action == 'next_turn':
            global_simulation.iterate()
            store_to_db(global_simulation)
        elif action == 'reset':
            db.drop_all()
            db.create_all()
            db.session.commit()
        else:
            print(f'unknown action: {action}')

    simulation_count = len(global_simulation.simulations)

    return render_template('index.html', simulation_count=simulation_count)

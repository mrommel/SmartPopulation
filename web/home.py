"""General page routes."""
from flask import Blueprint, request, make_response
from flask import render_template

from . import db
from .models import Simulations

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
            # sim = simulation_from_database()
            # sim.iterate()
            # simulation_to_database(sim)
            pass
        elif action == 'reset':
            db.drop_all()
            db.create_all()
            db.session.commit()
        else:
            print(f'unknown action: {action}')

        simulation_count = len(Simulations.query.all())
    else:
        simulation_count = len(Simulations.query.all())

    return render_template('index.html', simulation_count=simulation_count)

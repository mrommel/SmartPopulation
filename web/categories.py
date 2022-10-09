"""Categories page routes."""

from flask import Blueprint
from flask import render_template

from simulation.base import SimulationCategory
from simulation.simulation import Simulation

# from web import simulation_from_database

# Blueprint Configuration
categories_blueprint = Blueprint(
    "categories_blueprint", __name__, template_folder="templates", static_folder="static"
)


@categories_blueprint.route("/categories")
def categories():
    category_items = SimulationCategory

    return render_template('categories.html', categories=category_items)


@categories_blueprint.route('/category/<key>')
def category(key):
    sim = Simulation()  # simulation_from_database()
    category_item = SimulationCategory[key]

    category_item.simulation_list = category_item.simulations(sim)
    category_item.situation_list = category_item.situations(sim)
    category_item.policy_list = category_item.policies(sim)

    return render_template('category.html', category=category_item)
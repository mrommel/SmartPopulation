"""Simulations page routes."""
import json

import pandas as pd
import plotly
import plotly.express as px
from flask import Blueprint
from flask import render_template

from web import global_simulation
from web.utils import color_for

# Blueprint Configuration
simulations_blueprint = Blueprint(
    "simulations_blueprint", __name__, template_folder="templates", static_folder="static"
)


@simulations_blueprint.route("/simulations")
def simulations():

    # enrich simulations
    for key, simulation_item in global_simulation.simulations.items():
        simulation_item.prop = color_for(simulation_item.value)

    return render_template('simulations.html', simulations=global_simulation.simulations)


@simulations_blueprint.route('/simulation_callback', methods=[' POST', 'GET'])
def cb():
    # request.args.get('data')

    key = 'air_travel'
    simulation_item = global_simulation.simulations[key]
    return simulation_history(simulation_item)


@simulations_blueprint.route('/simulation/<key>')
def simulation(key):

    simulation_item = global_simulation.simulations[key]

    # enrich the simulation
    simulation_item.prop = color_for(simulation_item.value)
    simulation_item.cause_list = simulation_item.cause_values(global_simulation)
    simulation_item.effect_list = simulation_item.effect_values(global_simulation)

    return render_template(
        'simulation.html', simulation=simulation_item, graph_json=simulation_history(simulation_item))


def simulation_history(simulation_item):
    data = simulation_item.history  # list(reversed(simulation_item.history))
    d = {"iteration": range(0, len(data)), "value": data}
    df = pd.DataFrame(d)

    fig = px.line(
        df,
        title="History",
        x="iteration",
        y="value",
        range_y=[0.0, 1.0],
        template="plotly_dark"
    )
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json

"""Simulations page routes."""
import json

import pandas as pd
import plotly
import plotly.express as px
from flask import Blueprint
from flask import render_template

from web import simulation_from_database

# Blueprint Configuration
simulations_blueprint = Blueprint(
    "simulations_blueprint", __name__, template_folder="templates", static_folder="static"
)


@simulations_blueprint.route("/simulations")
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


@simulations_blueprint.route('/simulation_callback', methods=[' POST', 'GET'])
def cb():
    # request.args.get('data')
    sim = simulation_from_database()

    key = 'air_travel'
    simulation_item = sim.simulations[key]
    return simulation_history(simulation_item)


@simulations_blueprint.route('/simulation/<key>')
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

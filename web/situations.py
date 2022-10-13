"""Situations page routes."""
import json

import pandas as pd
import plotly
import plotly.express as px
from flask import Blueprint
from flask import render_template

from simulation.simulation import Simulation
from web import global_simulation

# from web import simulation_from_database

# Blueprint Configuration
situations_blueprint = Blueprint(
    "situations_blueprint", __name__, template_folder="templates", static_folder="static"
)


@situations_blueprint.route("/situations")
def situations():

    # enrich simulations
    for key, situation_item in global_simulation.situations.items():
        if situation_item.is_active:
            situation_item.prop = 'bg-success'
        else:
            situation_item.prop = 'bg-danger'

    return render_template('situations.html', situations=global_simulation.situations)


@situations_blueprint.route('/situation/<key>')
def situation(key):

    situation_item = global_simulation.situations[key]

    # enrich the simulation
    if situation_item.is_active:
        situation_item.prop = 'bg-success'
    else:
        situation_item.prop = 'bg-danger'

    situation_item.input_list = situation_item.input_values(global_simulation)
    situation_item.effect_list = situation_item.effect_values(global_simulation)

    return render_template('situation.html', situation=situation_item, graph_json=situation_history(situation_item))


def situation_history(situation_item):
    data = situation_item.history  # list(reversed(simulation_item.history))
    d = {
        'iteration': range(0, len(data)),
        'value': data,
        'start': [situation_item.start_trigger] * len(data),
        'end': [situation_item.end_trigger] * len(data)
    }
    df = pd.DataFrame(d)

    fig = px.line(
        df,
        title='History',
        x='iteration',
        y=['value', 'start', 'end'],
        range_y=[0.0, 1.0],
        template='plotly_dark'
    )
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json

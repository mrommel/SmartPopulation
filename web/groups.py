"""Groups page routes."""

from flask import Blueprint
from flask import render_template

# from web import simulation_from_database

# Blueprint Configuration
groups_blueprint = Blueprint(
    "groups_blueprint", __name__, template_folder="templates", static_folder="static"
)


@groups_blueprint.route("/groups")
def groups():
    sim = Simulation()  # simulation_from_database()

    # enrich simulations
    for key, group_item in sim.groups.items():
        if group_item.mood.value > 0.8:
            group_item.mood_prop = 'bg-success'
        elif group_item.mood.value > 0.6:
            group_item.mood_prop = 'bg-primary'
        elif group_item.mood.value > 0.4:
            group_item.mood_prop = 'bg-warning'
        elif group_item.mood.value > 0.2:
            group_item.mood_prop = 'bg-orange'
        else:
            group_item.mood_prop = 'bg-danger'

        if group_item.freq.value > 0.8:
            group_item.freq_prop = 'bg-success'
        elif group_item.freq.value > 0.6:
            group_item.freq_prop = 'bg-primary'
        elif group_item.freq.value > 0.4:
            group_item.freq_prop = 'bg-warning'
        elif group_item.freq.value > 0.2:
            group_item.freq_prop = 'bg-orange'
        else:
            group_item.freq_prop = 'bg-danger'

    return render_template('groups.html', groups=sim.groups)


@groups_blueprint.route("/group/<key>")
def group(key):
    sim = Simulation()  # simulation_from_database()

    group_item = sim.groups[key]

    if group_item.mood.value > 0.8:
        group_item.mood_prop = 'bg-success'
    elif group_item.mood.value > 0.6:
        group_item.mood_prop = 'bg-primary'
    elif group_item.mood.value > 0.4:
        group_item.mood_prop = 'bg-warning'
    elif group_item.mood.value > 0.2:
        group_item.mood_prop = 'bg-orange'
    else:
        group_item.mood_prop = 'bg-danger'

    if group_item.freq.value > 0.8:
        group_item.freq_prop = 'bg-success'
    elif group_item.freq.value > 0.6:
        group_item.freq_prop = 'bg-primary'
    elif group_item.freq.value > 0.4:
        group_item.freq_prop = 'bg-warning'
    elif group_item.freq.value > 0.2:
        group_item.freq_prop = 'bg-orange'
    else:
        group_item.freq_prop = 'bg-danger'

    group_item.mood.input_list = group_item.mood.input_values(sim)
    group_item.freq.input_list = group_item.freq.input_values(sim)

    return render_template('group.html', group=group_item)
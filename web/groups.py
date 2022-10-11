"""Groups page routes."""

from flask import Blueprint
from flask import render_template

from web import global_simulation

# Blueprint Configuration
groups_blueprint = Blueprint(
    "groups_blueprint", __name__, template_folder="templates", static_folder="static"
)


@groups_blueprint.route("/groups")
def groups():

    # enrich simulations
    for key, group_item in global_simulation.groups.items():
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

    return render_template('groups.html', groups=global_simulation.groups)


@groups_blueprint.route("/group/<key>")
def group(key):

    group_item = global_simulation.groups[key]

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

    group_item.mood.input_list = group_item.mood.input_values(global_simulation)
    group_item.freq.input_list = group_item.freq.input_values(global_simulation)

    return render_template('group.html', group=group_item)
"""Groups page routes."""

from flask import Blueprint
from flask import render_template

from web import global_simulation
from web.utils import color_for

# Blueprint Configuration
groups_blueprint = Blueprint(
	"groups_blueprint", __name__, template_folder="templates", static_folder="static"
)


@groups_blueprint.route("/groups")
def groups():
	# enrich simulations
	for _, group_item in global_simulation.groups.items():
		group_item.mood_prop = color_for(group_item.mood.value)
		group_item.freq_prop = color_for(group_item.freq.value)

	return render_template('groups.html', groups=global_simulation.groups)


@groups_blueprint.route("/group/<key>")
def group(key):
	group_item = global_simulation.groups[key]

	group_item.mood_prop = color_for(group_item.mood.value)
	group_item.freq_prop = color_for(group_item.freq.value)

	group_item.mood.cause_list = group_item.mood.cause_values(global_simulation)
	group_item.freq.cause_list = group_item.freq.cause_values(global_simulation)

	return render_template('group.html', group=group_item)

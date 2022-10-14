"""Policies page routes."""

from flask import Blueprint, request
from flask import render_template

from simulation.simulation import Simulation
from web import global_simulation
from web.models import store_to_db

# Blueprint Configuration
policies_blueprint = Blueprint(
    "policies_blueprint", __name__, template_folder="templates", static_folder="static"
)


@policies_blueprint.route("/policies")
def policies():
    """
        show an overview of all policies
    """

    return render_template('policies.html', policies=global_simulation.policies)


@policies_blueprint.route('/policy/<key>', methods=('GET', 'POST'))
def policy(key):
    """
        show single policy and when POSTed it updates the slider aka value of the policy
    """
    if request.method == 'POST':

        action = request.form['action']
        slider_value = request.form['slider']

        if action == 'change':
            policy_item = global_simulation.policies[key]
            policy_item.slider_value = slider_value

            # determine value
            step_value = 1.0 / len(policy_item.slider)

            try:
                slider_index = policy_item.slider.index(slider_value)
                policy_item.value = step_value * (slider_index + 1.0)
                # print(f'Update policy "{key}" to {policy_item.value} / index: {slider_index} / {slider_value}')
            except ValueError:
                print(f'Could not find {slider_value} in {policy_item.slider}')

            store_to_db(global_simulation)
        else:
            print(f'unknown action: {action}')

    policy_item = global_simulation.policies[key]

    policy_item.effect_list = policy_item.effect_values(global_simulation)

    return render_template('policy.html', policy=policy_item)

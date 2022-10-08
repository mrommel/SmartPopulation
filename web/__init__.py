import os

from flask import Flask
from flask_assets import Environment

from web.db import get_db, simulation_from_database, simulation_to_database, init_db, populate_db


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Database @todo: move to config - but how?
    app.config['DATABASE'] = os.path.join(app.instance_path, 'flaskr.sqlite')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    assets = Environment()
    assets.init_app(app)

    from . import db
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .assets import compile_static_assets

        # register some template filters
        from . import utils

        # from . import routes
        from . import home
        from . import simulations
        from . import groups
        from . import situations
        from . import policies
        from . import categories

        # Register Blueprints
        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(simulations.simulations_blueprint)
        app.register_blueprint(groups.groups_blueprint)
        app.register_blueprint(situations.situations_blueprint)
        app.register_blueprint(policies.policies_blueprint)
        app.register_blueprint(categories.categories_blueprint)

        # Compile static assets
        compile_static_assets(assets)

    return app

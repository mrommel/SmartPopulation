import sqlite3
import click
from flask import current_app, g

from simulation.base import SimulationCategory
from simulation.simulation import Simulation


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        
    
def populate_db():
    db = get_db()

    sim = Simulation()

    for category in SimulationCategory:
        db.execute(
            'INSERT INTO categories (id, name)'
            ' VALUES (?, ?)',
            (category.value, category.name)
        )
        db.commit()

    for key, simulation in sim.simulations.items():
        db.execute(
            'INSERT INTO simulations (name, description, category_id, value, min_value, max_value)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (simulation.name, simulation.description, simulation.category.value, simulation.value,
             simulation.min_value, simulation.max_value)
        )
        db.commit()

    for key, situation in sim.situations.items():
        db.execute(
            'INSERT INTO situations (name, description)'
            ' VALUES (?, ?)',
            (situation.name, situation.description)
        )
        db.commit()
    

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    populate_db()
    click.echo('Initialized the database.')
    
    
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
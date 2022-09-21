import sqlite3
import click
from flask import current_app, g

from simulation.base import SimulationCategory, SimulationBase
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
            'INSERT INTO simulations (key, name, description, category_id, value, min_value, max_value)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?)',
            (key, simulation.name, simulation.description, simulation.category.value, simulation.value,
             simulation.min_value, simulation.max_value)
        )
        db.commit()

    for key, situation in sim.situations.items():
        db.execute(
            'INSERT INTO situations (key, name, description)'
            ' VALUES (?, ?, ?)',
            (key, situation.name, situation.description)
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


def simulation_from_database() -> Simulation:
    database = get_db()
    
    sim = Simulation()
    
    sim.simulations.clear()
    
    # populate simulations
    simulation_items = database.execute(
        'SELECT '
        '  s.id, s.key, s.name AS name, s.description, s.category_id, s.value, s.min_value, s.max_value '
        'FROM '
        '  simulations AS s'
    ).fetchall()
    
    for simulation_item in simulation_items:
        simulation_obj = SimulationBase(
            name=simulation_item['name'],
            description=simulation_item['description'],
            category=simulation_item['category_id'],
            default_value=simulation_item['value'],
            min_value=simulation_item['min_value'],
            max_value=simulation_item['max_value']
        )
        sim.simulations[simulation_item['key']] = simulation_obj
        print(f"added: {simulation_item['key']} = {simulation_item['name']}")
    
    return sim

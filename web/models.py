"""Data models."""
from sqlalchemy import event

from simulation.simulation import Simulation
from . import db


class Simulations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), index=False, unique=True, nullable=False)
    value = db.Column(db.Float)

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "<Simulation {} = {}>".format(self.key, self.value)


@event.listens_for(Simulations.__table__, 'after_create')
def create_simulations(*args, **kwargs):
    sim = Simulation()

    for key, simulation in sim.simulations.items():
        db.session.add(Simulations(key=key, value=simulation.default_value))

    db.session.commit()

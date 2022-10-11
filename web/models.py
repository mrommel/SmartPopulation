"""Data models."""
from sqlalchemy import event, UniqueConstraint

from simulation.simulation import Simulation
from . import db


class Simulations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32), index=False, unique=True, nullable=False)
    value = db.Column(db.Float)
    historic_values = db.relationship('SimulationsHistory', backref='simulation', lazy='dynamic')

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        values_str = [str(historic_value) for historic_value in self.historic_values]
        return "<Simulations {} ({}) = {} ({})>".format(self.key, self.id, self.value, values_str)


@event.listens_for(Simulations.__table__, 'after_create')
def create_simulations(*args, **kwargs):
    sim = Simulation()

    for key, simulation in sim.simulations.items():
        db.session.add(Simulations(key=key, value=simulation.default_value))

    db.session.commit()


class SimulationsHistory(db.Model):
    __table_args__ = (UniqueConstraint('simulation_id', 'iteration', name='simulation_iteration'),)
    id = db.Column(db.Integer, primary_key=True)
    simulation_id = db.Column(db.Integer, db.ForeignKey('simulations.id'), nullable=False)
    iteration = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float)

    def __init__(self, simulation_id, iteration, value):
        self.simulation_id = simulation_id
        self.iteration = iteration
        self.value = value

    def __repr__(self):
        return "<SimulationsHistory {} ({}) = {}>".format(self.simulation_id, self.iteration, self.value)


class Situations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32), index=False, unique=True, nullable=False)
    is_active = db.Column(db.Boolean)
    historic_values = db.relationship('SituationsHistory', backref='situation', lazy='dynamic')

    def __init__(self, key, is_active):
        self.key = key
        self.is_active = is_active

    def __repr__(self):
        values_str = [str(historic_value) for historic_value in self.historic_values]
        return "<Situations {} = {} => ({})>".format(self.key, self.is_active, values_str)


@event.listens_for(Situations.__table__, 'after_create')
def create_situations(*args, **kwargs):
    sim = Simulation()

    for key, situation in sim.situations.items():
        db.session.add(Situations(key=key, is_active=situation.is_active))

    db.session.commit()


class SituationsHistory(db.Model):
    __table_args__ = (UniqueConstraint('situation_id', 'iteration', name='situation_iteration'),)
    id = db.Column(db.Integer, primary_key=True)
    situation_id = db.Column(db.Integer, db.ForeignKey('situations.id'), nullable=False)
    iteration = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float)

    def __init__(self, situation_id, iteration, value):
        self.situation_id = situation_id
        self.iteration = iteration
        self.value = value

    def __repr__(self):
        return "<SituationsHistory {} ({}) = {}>".format(self.situation_id, self.iteration, self.value)


class Policies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32), index=False, unique=True, nullable=False)
    is_active = db.Column(db.Boolean)
    slider_value = db.Column(db.String(32))
    value = db.Column(db.Float)

    def __init__(self, key, is_active, slider_value, value):
        self.key = key
        self.is_active = is_active
        self.slider_value = slider_value
        self.value = value

    def __repr__(self):
        return "<Policies {} = {}, {}, {}>".format(self.key, self.is_active, self.slider_value, self.value)


@event.listens_for(Policies.__table__, 'after_create')
def create_policies(*args, **kwargs):
    sim = Simulation()

    for key, policy in sim.policies.items():
        db.session.add(
            Policies(
                key=key,
                is_active=policy.is_active,
                slider_value=policy.slider_value,
                value=policy.value
            )
        )

    db.session.commit()


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32), index=False, unique=True, nullable=False)
    mood = db.Column(db.Float)
    freq = db.Column(db.Float)

    def __init__(self, key: str, mood: float, freq: float):
        self.key = key
        self.mood = mood
        self.freq = freq

    def __repr__(self):
        return "<Groups {} = {}, {}>".format(self.key, self.mood, self.freq)


@event.listens_for(Groups.__table__, 'after_create')
def create_groups(*args, **kwargs):
    sim = Simulation()

    for key, group in sim.groups.items():
        db.session.add(Groups(key, group.mood.value, group.freq.value))

    db.session.commit()


def load_from_db(sim: Simulation):
    # populate simulations
    for simulations_item in Simulations.query.all():
        sim.simulations[simulations_item.key].value = simulations_item.value

    # populate simulations history
    for simulations_history_item in SimulationsHistory.query.all():
        sim.simulations[simulations_history_item.simulation.key].history.insert(0, simulations_history_item.value)

    # populate situations
    for situations_item in Situations.query.all():
        sim.situations[situations_item.key].is_active = situations_item.is_active

    # populate situations history
    for situations_history_item in SituationsHistory.query.all():
        sim.situations[situations_history_item.situation.key].history.insert(0, situations_history_item.value)

    # populate policies
    for policies_item in Policies.query.all():
        sim.policies[policies_item.key].is_active = policies_item.is_active
        sim.policies[policies_item.key].slider_value = policies_item.slider_value
        sim.policies[policies_item.key].value = policies_item.value

    # populate policies history

    # populate groups
    for groups_item in Groups.query.all():
        sim.groups[groups_item.key].mood.value = groups_item.mood
        sim.groups[groups_item.key].freq.value = groups_item.freq

    # populate groups history

    return sim


def store_to_db(sim: Simulation):

    # delete all history values
    SimulationsHistory.query.delete()
    SituationsHistory.query.delete()
    db.session.commit()

    # simulations
    for key, simulation in sim.simulations.items():
        simulation_item = Simulations.query.filter_by(key=key).first()
        simulation_id = simulation_item.id

        if simulation_item is None:
            raise Exception(f'cant find simulation "{key}" in db')

        # update simulation value
        simulation_item.value = simulation.value

        # write historic simulation values into db
        for index, simulation_history_value in enumerate(simulation.history):
            new_simulation_history = SimulationsHistory(simulation_id, index, simulation_history_value)
            db.session.add(new_simulation_history)

        db.session.commit()

    # debug
    # for simulations_item in Simulations.query.all():
    #    print(simulations_item)

    # situations
    for key, situation in sim.situations.items():
        situation_item = Situations.query.filter_by(key=key).first()
        situation_id = situation_item.id

        if situation_item is None:
            raise Exception(f'cant find situation "{key}" in db')

        # update simulation value
        situation_item.is_active = situation.is_active

        # write historic situation values into db
        for index, situation_history_value in enumerate(situation.history):
            new_situation_history = SituationsHistory(situation_id, index, situation_history_value)
            db.session.add(new_situation_history)

        db.session.commit()

    # debug
    for situation_item in Situations.query.all():
        print(situation_item)

    """

    
        database.execute(
            'UPDATE situations SET is_active = ? WHERE key = ?',
            (situation.is_active, key)
        )
        database.commit()

        situation_row = database.execute(
            'SELECT s.id FROM situations AS s WHERE key = ?',
            (key,)
        ).fetchone()
        situation_id = situation_row[0]

        database.execute(
            'DELETE FROM situation_histories WHERE situation_id = ?',
            (situation_id,)
        )
        database.commit()

        for situation_history_value in situation.history:
            database.execute(
                'INSERT INTO situation_histories (situation_id, value) VALUES (?, ?)',
                (situation_id, situation_history_value)
            )
            database.commit()

    # polices
    for key, policy in sim.policies.items():
        database.execute(
            'UPDATE policies SET is_active = ?, slider_value = ?, value = ? WHERE key = ?',
            (policy.is_active, policy.slider_value, policy.value, key)
        )
        database.commit()

        policy_row = database.execute(
            'SELECT p.id FROM policies AS p WHERE key = ?',
            (key,)
        ).fetchone()
        if policy_row is None:
            raise Exception(f'cant find policy "{key}" in db')

        policy_id = policy_row[0]

        database.execute(
            'DELETE FROM policy_histories WHERE policy_id = ?',
            (policy_id,)
        )
        database.commit()

        for policy_history_value in policy.history:
            database.execute(
                'INSERT INTO policy_histories (policy_id, value) VALUES (?, ?)',
                (policy_id, policy_history_value)
            )
            database.commit()

    # groups
    for key, group in sim.groups.items():

        group_row = database.execute(
            'SELECT g.id FROM groups AS g WHERE g.key = ?', (key,)
        ).fetchone()
        if group_row is None:
            raise Exception(f'cant find group "{key}" in db')

        group_id = group_row[0]

        database.execute(
            'DELETE FROM group_histories WHERE group_id = ?', (group_id,)
        )
        database.commit()

        for index in range(0, len(group.mood.history)):
            group_mood_history_value = group.mood.history[index]
            group_freq_history_value = group.mood.history[index]
            database.execute(
                'INSERT INTO group_histories (group_id, mood_value, freq_value) VALUES (?, ?, ?)',
                (group_id, group_mood_history_value, group_freq_history_value)
            )
            database.commit()
    """

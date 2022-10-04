"""life span simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class LifespanSimulation(SimulationBase):
	"""
		life span simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Lifespan",
			"",
			SimulationCategory.public_services,
			'simulation_default.png',
			0.5,
			emotion=SimulationEmotion.high_good
		)

		# Life span effects
		self.effects.append(SimulationConnection('retired_freq', '0 - (0.08 * x)'))
		# self.effects.append(SimulationConnection('food_price', '0 - (0.03 * x)'))

"""life span simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


class LifespanSimulation(SimulationBase):
	"""
		life span simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Lifespan",
			"",
			SimulationCategory.public_services,
			0.5
		)

		# connections:
		self.effects.append(SimulationConnection('retired_freq', '0 - (0.08 * x)'))
		# self.effects.append(SimulationConnection('food_price', '0 - (0.03 * x)'))

"""life span simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class LifespanSimulation(SimulationBase):
	"""
		life span simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Lifespan",
			"",
			SimulationCategory.public_services,
			'simulation_lifespan.png',
			0.5,
			emotion=SimulationEmotion.high_good
		)

		# Life span effects
		self.effects.append(Effect('retired_freq', '0 - (0.08 * x)'))
		# self.effects.append(Effect('food_price', '0 - (0.03 * x)'))

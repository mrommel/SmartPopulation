"""environment simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


class EnvironmentSimulation(SimulationBase):
	"""
		environment simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Environment",
			"A general measurement of the quality of the environment, including air quality, but also measuring noise "
			"pollution, litter, water quality and many other measures of pollution",
			SimulationCategory.public_services,
			0.50
		)
		
		# connections:
		self.effects.append(SimulationConnection('environmentalist_mood', '0.4 - (x * 0.8)'))
		self.effects.append(SimulationConnection('pollution', '1.0 - (1.0 * x)'))
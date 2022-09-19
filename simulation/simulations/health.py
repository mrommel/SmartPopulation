"""health simulation"""
from simulation.base import SimulationBase, SimulationCategory, SimulationConnection


class HealthSimulation(SimulationBase):
	"""
		health simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Health",
			"A general indicator for the health of your citizens that measures not just raw lifespan, but also fitness "
			"and the general well-being of people.",
			SimulationCategory.public_services,
			0.8
		)
		
		# connections
		self.effects.append(SimulationConnection('retired_freq', '-0.2 - (0.4 * x)', 8))
		self.effects.append(SimulationConnection('worker_productivity', '-0.15 + (0.15 * x)'))
		self.effects.append(SimulationConnection('immigration', '0.1 * (x ** 6.0)'))

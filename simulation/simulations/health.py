"""health simulation"""
from simulation.base import SimulationBase, SimulationCategory, Effect, SimulationEmotion


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
			'simulation_health.png',
			0.8,
			emotion=SimulationEmotion.high_good
		)
		
		# connections
		self.effects.append(Effect('retired_freq', '-0.2 - (0.4 * x)', 8))
		self.effects.append(Effect('worker_productivity', '-0.15 + (0.15 * x)'))
		self.effects.append(Effect('immigration', '0.1 * (x ** 6.0)'))
		self.effects.append(Effect('lifespan', '0.0 + (0.65 * x)', 4))

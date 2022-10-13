"""working week simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class WorkingWeekSimulation(SimulationBase):
	"""
		working week simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Working Week",
			"The number of hours worked on average by your citizens in a week. In a fluctuating economy, this may vary "
			"from the contracted hours as people give into pressure to work unpaid or paid overtime to keep their "
			"jobs. To employees, shorter hours are seen as a good thing.",
			SimulationCategory.economy,
			'simulation_working_week.png',
			0.5,
			emotion=SimulationEmotion.unknown
		)

		# connections:
		self.effects.append(Effect('trade_unionist_mood', '0.1 - (0.1 * x)'))
		self.effects.append(Effect('health', '-0.24 * (x ** 8)'))

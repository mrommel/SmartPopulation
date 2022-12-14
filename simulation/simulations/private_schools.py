"""private schools simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class PrivateSchoolsSimulation(SimulationBase):
	"""
		private schools simulation
	"""

	def __init__(self):
		super().__init__(
			"Private Schools",
			"The size of the private education sector. This will contract if the state provides a high quality system "
			"of state education. In tough economic times, there will be many in society who cannot afford private "
			"education.",
			SimulationCategory.public_services,
			'simulation_default.png',
			0.5,
			emotion=SimulationEmotion.high_bad
		)

		# connections:
		self.effects.append(Effect('_middle_income', '0.0 - (0.08 * x)'))
		self.effects.append(Effect('education', '0.05 + (0.15 * x)', 8))
		self.effects.append(Effect('unemployment', '0.0 - (0.13 * x)'))
		self.effects.append(Effect('capitalist_mood', '0.0 + (0.1 * x)'))
		self.effects.append(Effect('trade_unionist_mood', '0.0 - (0.1 * x)'))
		self.effects.append(Effect('religious_freq', '0 + (0.2 * x)', 10))

"""
	situation of pollution
"""
from simulation.base import SituationBase, SimulationCategory, SimulationConnection


class PollutionSituation(SituationBase):
	"""
		situation of pollution
	"""
	
	def __init__(self):
		super().__init__(
			'Pollution',
			'Without enough measures in place to regulate what gets pumped into the air, we have ended up with high '
			'levels of pollution. This affects our health levels and quality of life. Not surprisingly '
			'environmentalists are especially upset.',
			'We have a serious pollution problem. This could lead to health problems.',
			'Environmental experts tell us that the country\'s pollution problem is now under control, our citizens no '
			'longer need to wear face-masks when cycling to work!',
			SimulationCategory.economy,
			0.0,
			0.6,
			0.4
		)

		# connections
		self.effects.append(SimulationConnection('health', '0 - (0.48 * x) ** 1.5'))
		self.effects.append(SimulationConnection('environmentalist_mood', '-0.1 - (0.3 * x)'))
		self.effects.append(SimulationConnection('environmentalist_freq', '0.1 + (0.1 * x)'))
		self.effects.append(SimulationConnection('tourism', '-0.03 - (0.03 * x)', 4))
	
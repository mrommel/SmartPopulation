"""
	situation of high productivity
"""
from simulation.base import SituationBase, SimulationCategory, Effect


class HighProductivitySituation(SituationBase):
	"""
		situation of high productivity
	"""
	
	def __init__(self):
		super().__init__(
			'High Productivity',
			'Our workforce are extremely productive, producing a higher amount of practically everything in comparison '
			'with our competitors. This is great news for the future of our economy.',
			'Business pundits report that our companies are highly efficient and productive in comparison with '
			'competing nations.',
			'Our workers\' productivity has fallen and sadly, we are no longer considered to be a nation with '
			'especially high productivity. Global corporations may rethink setting up factories here, and this will '
			'adversely affect our economy.',
			SimulationCategory.economy,
			0.0,  # default
			0.6,
			0.4
		)
		
		# input
		
		# effects
		self.effects.append(Effect('gdp', '0.04 + (0.03 * x)'))
		self.effects.append(Effect('self_employed_mood', '0.0 + (0.1 * x)'))
		self.effects.append(Effect('capitalist_mood', '0.0 + (0.1 * x)'))
		# self_employed_income,0+(0.08*x)

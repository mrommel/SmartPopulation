"""
	gambling policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class GamblingPolicy(PolicyBase):
	"""
		gambling policy
	"""
	
	def __init__(self):
		super().__init__(
			"Gambling",
			"To some, gambling is a sin which leads to poverty and disaster, but others believe that some 'social' "
			"gambling is harmless fun which can also be taxed nicely by the government as an additional form of "
			"revenue. It also encourages tourism and creates jobs.	",
			category=SimulationCategory.law_and_order,
			slider=['LIMITED STAKES, AGE LIMIT', 'NO STAKES LIMIT', 'NO RESTRICTIONS'],
			can_be_cancelled=True,
			introduce=27,  # in political capital
			cancel=32,  # in political capital
			raise_cost=19,  # in political capital
			lower_cost=14,  # in political capital
			min_cost=0,
			max_cost=0,
			implementation=3,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # no costs
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'NO STAKES LIMIT'
		self.value = 0.5
		
		# connections:
		self.effects.append(SimulationConnection('liberal_mood', '0.00 + (0.08 * x)'))
		self.effects.append(SimulationConnection('religious_mood', '0.00 - (0.15 * x)'))
		self.effects.append(SimulationConnection('gdp', '0.00 + (0.04 * x)', 6))
		self.effects.append(SimulationConnection('unemployment', '0.00 - (0.03 * x)', 4))
		self.effects.append(SimulationConnection('capitalist_mood', '0.01 + (0.04 * x)'))
		self.effects.append(SimulationConnection('organised_crime', '0.0 + (0.45 * x)'))
		
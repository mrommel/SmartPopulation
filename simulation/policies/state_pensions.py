"""
	state pension policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class StatePensionsPolicy(PolicyBase):
	"""
		state pension policy
	"""
	
	def __init__(self):
		super().__init__(
			"State Pensions	",
			"Rather than leave it up to the individual to provide for themselves after retirement, state pensions can "
			"guarantee a minimum standard of living for the elderly. Be aware that as life expectancy rises, "
			"the cost to the state of paying out pensions increases hugely. The level of state pension may encourage "
			"or discourage citizens to save into private pension plans.",
			category=SimulationCategory.welfare,
			slider=['NONE',	'LOW', 'MEDIUM', 'HIGH', 'MAXIMUM'],
			can_be_cancelled=True,
			introduce=19,  # in political capital
			cancel=49,  # in political capital
			raise_cost=9,  # in political capital
			lower_cost=26,  # in political capital
			min_cost=2500,
			max_cost=14000,
			implementation=2,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # _default_,1.0;Health,0.2*(x^6)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'HIGH'
		self.value = 0.8
		
		# connections:
		self.effects.append(SimulationConnection('capitalist_mood', '-0.02 - (0.1 * x)'))
		self.effects.append(SimulationConnection('retired_mood', '0.2 + (0.55 * x)'))
		self.effects.append(SimulationConnection('poor_mood', '0.07 + (0.12 * x)'))
		self.effects.append(SimulationConnection('poverty_rate', '0.0 - (0.2 * x)'))
		# retired_income,0.1+(0.2*x)
		# _global_socialism,0.02+(0.02*x),12
		self.effects.append(SimulationConnection('retired_freq', '0.0 + (0.09 * x)', 8))

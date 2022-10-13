"""
	unemployed benefit policy
"""
from simulation.base import SimulationCategory, PolicyBase, Effect, SimulationEmotion


class UnemployedBenefitPolicy(PolicyBase):
	"""
		unemployed benefit policy
	"""
	
	def __init__(self):
		super().__init__(
			"Unemployed Benefit",
			"Unemployment benefit is a state benefit given to everyone who is able to work but cannot find employment. "
			"Socialists regard this as a minimum safety net for workers out of work because of the whims of the "
			"economy. Some believe that high unemployment benefits distort the market and discourage people from "
			"seeking work.",
			category=SimulationCategory.welfare,
			slider=['NONE',	'LOW', 'MEDIUM', 'HIGH', 'MAXIMUM'],
			can_be_cancelled=True,
			introduce=25,  # in political capital
			cancel=27,  # in political capital
			raise_cost=14,  # in political capital
			lower_cost=12,  # in political capital
			min_cost=500,
			max_cost=5440,
			implementation=1,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # Unemployment,0+(1.0*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'HIGH'
		self.value = 0.8
		
		# connections:
		self.effects.append(Effect('capitalist_mood', '-0.01 - (0.08 * x)'))
		self.effects.append(Effect('unemployment', '0.0 + (0.1 * x)', 8))
		self.effects.append(Effect('poor_mood', '0.1 + (0.3 * x)'))
		self.effects.append(Effect('socialist_mood', '0.0 + (0.15 * x)'))
		self.effects.append(Effect('poverty_rate', '0.0 - (0.12 * x)'))
		self.effects.append(Effect('_low_income', '0.0 + (0.15 * x)'))
		self.effects.append(Effect('black_market', '0.0 - (0.2 * x)'))

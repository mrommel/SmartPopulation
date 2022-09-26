"""
	state health service policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class StateHealthServicePolicy(PolicyBase):
	"""
		state health service policy
	"""
	
	def __init__(self):
		super().__init__(
			"State Health Service",
			"Although many citizens would be happy to pay privately for their own health treatment, there is an "
			"argument that the state has a duty to provide a minimum level of free health treatment for everyone "
			"regardless of income. Health provision can be expensive, so it's a matter of debate as to how much should "
			"be spent.",
			category=SimulationCategory.public_services,
			slider=['LIFE THREATENING OPS', 'ALL MAJOR OPERATIONS', 'SERIOUS ILLNESS ONLY', 'SOME PREVENTION', 'EXCELLENT HEALTH PROVISION'],
			can_be_cancelled=True,
			introduce=38,  # in political capital
			cancel=60,  # in political capital
			raise_cost=18,  # in political capital
			lower_cost=26,  # in political capital
			min_cost=3000,
			max_cost=12000,
			implementation=12,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # _default_,0.6;TobaccoUse,0+(0.16*x);Environment,0.2-(0.1*x);Alcoholism,0.1+(0.1*x);Wages,-0.1+(0.2*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'SOME PREVENTION'
		self.value = 0.8
		
		# connections:
		self.effects.append(SimulationConnection('poor_mood', '0.05 + (0.15 * x)'))
		self.effects.append(SimulationConnection('capitalist_mood', '-0.02 - (0.10 * x)'))
		self.effects.append(SimulationConnection('wealthy_mood', '0.00 - (0.10 * x)'))
		self.effects.append(SimulationConnection('socialist_mood', '0.05 + (0.11 * x)'))
		self.effects.append(SimulationConnection('health', '0.25 * (x ** 0.6) + 0.05', 4))
		self.effects.append(SimulationConnection('retired_mood', '0.0 + (0.16 * x)'))
		self.effects.append(SimulationConnection('unemployment', '0.0 - (0.19 * x)'))
		self.effects.append(SimulationConnection('state_employees_mood', '0.0 + (0.22 * x)'))
		self.effects.append(SimulationConnection('state_employees_freq', '0.0 + (0.1 * x)'))
		# state_employees_income,0+(0.09*x)
		# _global_socialism,0+(0.052*x),4


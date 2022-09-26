"""
	prisons policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class PrisonsPolicy(PolicyBase):
	"""
		prisons policy
	"""
	
	def __init__(self):
		super().__init__(
			"Prisons",
			"Some argue that providing the minimum number of bare, cold cells is the only provision that needs to be "
			"made for those who have broken the law. Others suggest that spending more money allows for prisoners to "
			"be rehabilitated as well as punished and reduces the chances of re-offending.",
			category=SimulationCategory.law_and_order,
			slider=['OVERCROWDED CELLS', 'SHARED CELLS', 'BASIC PROVISION', 'SOME RE-EDUCATION', 'EXTENSIVE REHABILITATION'],
			can_be_cancelled=False,
			introduce=13,  # in political capital
			cancel=20,  # in political capital
			raise_cost=7,  # in political capital
			lower_cost=8,  # in political capital
			min_cost=100,
			max_cost=1920,
			implementation=6,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # CrimeRate,0.1+(0.9*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'SOME RE-EDUCATION'
		self.value = 0.8
		
		# connections:
		self.effects.append(SimulationConnection('crime_rate', '0.00 - (0.07 * x)', 8))
		self.effects.append(SimulationConnection('liberal_mood', '0.12 * (x ** 4)'))
		self.effects.append(SimulationConnection('conservatives_mood', '0.00 + (0.12 * x)'))
		self.effects.append(SimulationConnection('state_employees_mood', '0.0 + (0.15 * x)'))
		self.effects.append(SimulationConnection('state_employees_freq', '-0.05 + (0.1 * x)'))
		self.effects.append(SimulationConnection('unemployment', '0.0 - (0.02 * x)'))

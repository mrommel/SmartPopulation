"""
	armed police policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class ArmedPolicePolicy(PolicyBase):
	"""
		armed police policy
	"""
	
	def __init__(self):
		super().__init__(
			"Armed Police	",
			"Arming police officers can be an effective strategy in deterring crime and maintaining order. Opponents "
			"would argue that it encourages criminals to use firearms in a 'criminal arms race'. Critics also worry "
			"that arming the police will distance them from law-abiding citizens.",
			category=SimulationCategory.law_and_order,
			slider=['SPECIALISTS', 'IN EVERY DEPT',	'WIDESPREAD', 'EVERY OFFICER ARMED', 'SUBMACHINEGUNS'],
			can_be_cancelled=False,
			introduce=50,  # in political capital
			cancel=48,  # in political capital
			raise_cost=10,  # in political capital
			lower_cost=19,  # in political capital
			min_cost=300,
			max_cost=960,
			implementation=3,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # no costs
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'EVERY OFFICER ARMED'
		self.value = 0.8
		
		# connections:
		self.effects.append(SimulationConnection('liberal_mood', '-0.05 - (0.25 * x)'))
		self.effects.append(SimulationConnection('crime_rate', '-0.10 - (0.10 * x)'))
		self.effects.append(SimulationConnection('violent_crime_rate', '0.00 - (0.20 * x)'))

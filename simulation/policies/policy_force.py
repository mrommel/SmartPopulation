"""
	policy force policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class PoliceForcePolicy(PolicyBase):
	"""
		policy force policy
	"""
	
	def __init__(self):
		super().__init__(
			"Police Force",
			"Every government needs to employ a police force to ensure order is kept and laws are obeyed, "
			"but it's a matter of debate exactly how much should be spent on the police. Some favor a "
			"large force with police on every street corner, other prefer a more low-key and tolerant "
			"approach.",
			category=SimulationCategory.law_and_order,
			slider=['NONE',	'LOW', 'MEDIUM', 'HIGH', 'MAXIMUM'],
			can_be_cancelled=False,
			introduce=25,  # in political capital
			cancel=37,  # in political capital
			raise_cost=4,  # in political capital
			lower_cost=18,  # in political capital
			min_cost=300,
			max_cost=2320,
			implementation=6,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # _default_,1.0;Wages,-0.1+(0.2*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'HIGH'
		self.value = 0.8

		# connections:
		self.effects.append(SimulationConnection('crime_rate', '-0.35 * (x ** 0.6)', 4))
		self.effects.append(SimulationConnection('violent_crime_rate', '-0.52 * (x ** 0.6)', 3))
		self.effects.append(SimulationConnection('conservatives_mood', '-0.2 + (0.48 * x)'))
		self.effects.append(SimulationConnection('state_employees_mood', '-0.15 + (0.37 * x)'))
		self.effects.append(SimulationConnection('state_employees_freq', '-0.05 + (0.1 * x)'))
		# state_employees_income,-0.3+(0.09*x)
		self.effects.append(SimulationConnection('unemployment', '0 - (0.03 * x)'))
		self.effects.append(SimulationConnection('alcoholism', '0 - (0.6 * x) '))
		self.effects.append(SimulationConnection('street_gangs', '0-(0.17*x)', 4))

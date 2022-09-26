"""
	state school policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class StateSchoolsPolicy(PolicyBase):
	"""
		state school policy
	"""
	
	def __init__(self):
		super().__init__(
			"State Schools",
			"Free education for all ensures high levels of literacy and can be beneficial to the economy, especially "
			"those parts of the economy requiring a skilled workforce. The flipside of this is that state education "
			"can be expensive for the government. Wealthy individuals, not making use of state schools, may resent "
			"subsidizing them.	",
			category=SimulationCategory.public_services,
			slider=['WOODEN SCHOOLHUTS', 'SHARED TEXTBOOKS', 'MODERN TEXTBOOKS', 'STUDENT LAPTOPS'],
			can_be_cancelled=True,
			introduce=30,  # in political capital
			cancel=42,  # in political capital
			raise_cost=18,  # in political capital
			lower_cost=21,  # in political capital
			min_cost=1000,
			max_cost=10200,
			implementation=12,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # _default_,1.0;Wages,-0.1+(0.2*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'MODERN TEXTBOOKS'
		self.value = 0.8
		
		# connections:
		self.effects.append(SimulationConnection('poor_mood', '0.04 + (0.11 * x)'))
		self.effects.append(SimulationConnection('socialist_mood', '0.0 + (0.20 * x)'))
		self.effects.append(SimulationConnection('education', '0.3 * (x ** 0.6) + 0.07', 8))
		self.effects.append(SimulationConnection('poverty_rate', '-0.08 - (0.10 * x)'))
		self.effects.append(SimulationConnection('state_employees_mood', '0.0 + (0.14 * x)'))
		self.effects.append(SimulationConnection('unemployment', '0.0 - (0.19 * x)'))
		self.effects.append(SimulationConnection('state_employees_freq', '0.0 + (0.1 * x)'))
		# stateEmployees_income,0+(0.09*x)
		# _global_socialism,0+(0.03*x),12
		self.effects.append(SimulationConnection('parents_freq', '0.0 + (0.025 * x)', 8))

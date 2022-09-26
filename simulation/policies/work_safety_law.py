"""
	work safety law policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class WorkSafetyLawPolicy(PolicyBase):
	"""
		work safety law policy
	"""
	
	def __init__(self):
		super().__init__(
			"Work Safety Law",
			"Work safety law, often known as 'health and safety' is a series of measures to ensure employees are not "
			"at risk from injury in their day-to-day activities. Trade unionists often hail such laws as a valuable "
			"defense against unscrupulous employers who may put lives at risk. Many business leaders are concerned at "
			"the high levels of bureaucracy and restrictive practices that can result from such laws, which they see "
			"as a burden on business.	",
			category=SimulationCategory.economy,
			slider=['NONE', 'LOW', 'MEDIUM', 'HIGH', 'MAXIMUM'],
			can_be_cancelled=True,
			introduce=4,  # in political capital
			cancel=7,  # in political capital
			raise_cost=1,  # in political capital
			lower_cost=1,  # in political capital
			min_cost=10,
			max_cost=55,
			implementation=1,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # Unemployment,0+(1.0*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'HIGH'
		self.value = 0.8
		
		# connections:
		self.effects.append(SimulationConnection('trade_unionist_mood', '0.04 + (0.06 * x)'))
		self.effects.append(SimulationConnection('trade_unionist_freq', '0.02 + (0.02 * x)'))
		self.effects.append(SimulationConnection('self_employed_mood', '-0.05 - (0.08 * x)'))
		self.effects.append(SimulationConnection('self_employed_freq', '-0.02 - (0.08 * x)'))
		self.effects.append(SimulationConnection('worker_productivity', '-0.01 - (0.02 * x)', 4))
		self.effects.append(SimulationConnection('health', '0.01 + (0.02 * x)'))

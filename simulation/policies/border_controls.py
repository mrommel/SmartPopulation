"""
	border controls policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class BorderControlsPolicy(PolicyBase):
	"""
		border controls policy
	"""
	
	def __init__(self):
		super().__init__(
			"Border Controls",
			"Without some kind of customs checks at the borders, your country is open to the problem of mass illegal "
			"immigration. Some people argue that these immigrants cause crime, others that they take jobs away from "
			"your own citizens. Border controls can be effective in reducing illegal immigration.",
			category=SimulationCategory.foreign_policy,
			slider=['RANDOM PASSPORT CHECKS', 'PASSPORT CHECKS', 'BIOMETRIC CHECKS', 'ARMED GUARDS', 'RETINA SCANS'],
			can_be_cancelled=True,
			introduce=25,  # in political capital
			cancel=25,  # in political capital
			raise_cost=18,  # in political capital
			lower_cost=13,  # in political capital
			min_cost=10,
			max_cost=280,
			implementation=1,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # no costs
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'PASSPORT CHECKS'
		self.value = 0.2
		
		# connections:
		self.effects.append(SimulationConnection('patriot_mood', '0.0 + (0.30 * x)'))
		self.effects.append(SimulationConnection('liberal_mood', '0.0 - (0.225 * x)'))
		self.effects.append(SimulationConnection('immigration', '0.0 - (0.8 * x)', 2))
		self.effects.append(SimulationConnection('_terrorism', '0.0 - (0.1 * x)'))
		self.effects.append(SimulationConnection('ethnic_minorities_mood', '0.00 - (0.42 * x)'))
	
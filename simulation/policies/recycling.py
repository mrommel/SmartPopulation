"""
	recycling policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class RecyclingPolicy(PolicyBase):
	"""
		recycling policy
	"""
	
	def __init__(self):
		super().__init__(
			"Recycling",
			"Supporters of recycling argue that dumping waste in landfills just isn't a long term solution, "
			"and the government needs to show the way by providing facilities to recycle as many waste materials as "
			"possible. This might include recycling newspapers, cardboard, bottles and even some plastics.",
			category=SimulationCategory.economy,
			slider=[
				'POSTER CAMPAIGN', 'BOTTLE BANKS', 'RECYCLING CENTERS', 'LIMITED DOORSTEP COLLECTION',
				'UNIVERSAL DOORSTEP COLLECTION'
			],
			can_be_cancelled=True,
			introduce=13,  # in political capital
			cancel=18,  # in political capital
			raise_cost=4,  # in political capital
			lower_cost=4,  # in political capital
			min_cost=40,
			max_cost=400,
			implementation=5,
			min_income=0,
			max_income=0
		)
		
		self.cost_multiplier = []  # none
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'RECYCLING CENTERS'
		self.value = 0.5

		# connections:
		self.effects.append(SimulationConnection('environmentalist_mood', '0.04 + (0.09 * x)'))
		self.effects.append(SimulationConnection('environment', '0.01 + (0.04 * x)'))
		self.effects.append(SimulationConnection('environmentalist_freq', '0.02 + (0.08 * x)', 12))

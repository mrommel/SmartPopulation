"""
	inheritance tax policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class InheritanceTaxPolicy(PolicyBase):
	"""
		inheritance tax policy
	"""
	
	def __init__(self):
		super().__init__(
			"Inheritance Tax",
			"A tax paid on the wealth of an individual as it is passed on to their descendants. An inheritance tax "
			"protects equality, by preventing families amassing wealth and advantage over the generations, "
			"so it is popular with socialists and the poor. However, some people are strongly opposed to anything that "
			"prevents them handing on their hard-earned wealth, especially their house, to their children.",
			category=SimulationCategory.tax,
			slider=[
				'TAX0', 'TAX5', 'TAX10', 'TAX15', 'TAX20', 'TAX25', 'TAX30', 'TAX35', 'TAX40', 'TAX45', 'TAX50',
				'TAX55', 'TAX60', 'TAX65', 'TAX70', 'TAX75', 'TAX80', 'TAX85', 'TAX90', 'TAX95', 'TAX100'
			],
			can_be_cancelled=True,
			introduce=48,  # in political capital
			cancel=19,  # in political capital
			raise_cost=25,  # in political capital
			lower_cost=10,  # in political capital
			min_cost=0,
			max_cost=0,
			implementation=1,
			min_income=460,
			max_income=1683.6
		)
		
		self.cost_multiplier = []  #
		# income multiplier
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'TAX75'
		self.value = 0.75
		
		# connections:
		self.effects.append(SimulationConnection('wealthy_mood', '-0.1 - (0.25 * x)'))
		self.effects.append(SimulationConnection('socialist_mood', '0.0 + (0.2 * x)'))
		self.effects.append(SimulationConnection('equality', '0.1 + (0.3 * x)', 24))
		self.effects.append(SimulationConnection('conservatives_mood', '0.0 - (0.12 * x)'))
		self.effects.append(SimulationConnection('middle_income_mood', '0.0 - (0.18 * x)'))
		self.effects.append(SimulationConnection('_high_income', '0.0 - (0.12 * x)'))
		self.effects.append(SimulationConnection('retired_mood', '0.0 - (0.22 * x)'))
		# _global_socialism, 0 + (0.1 * x), 32



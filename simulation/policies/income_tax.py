"""
	income tax policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class IncomeTaxPolicy(PolicyBase):
	"""
		income tax policy
	"""
	
	def __init__(self):
		super().__init__(
			"Income Tax	",
			"One of the most popular ways to raise money for government is a direct tax on peoples earnings, "
			"deducted at source by their employer. Income tax is generally a progressive tax (the wealthy pay more as "
			"a fraction of their income than the poor) and for this reason it is popular with socialists and the low "
			"paid.",
			category=SimulationCategory.tax,
			slider=[
				'TAX0', 'TAX5', 'TAX10', 'TAX15', 'TAX20', 'TAX25', 'TAX30', 'TAX35', 'TAX40', 'TAX45', 'TAX50',
				'TAX55', 'TAX60', 'TAX65', 'TAX70', 'TAX75', 'TAX80', 'TAX85', 'TAX90', 'TAX95', 'TAX100'
			],
			can_be_cancelled=True,
			introduce=43,  # in political capital
			cancel=13,  # in political capital
			raise_cost=30,  # in political capital
			lower_cost=7,  # in political capital
			min_cost=0,
			max_cost=0,
			implementation=1,
			min_income=2300,
			max_income=123464
		)
		
		self.cost_multiplier = []  #
		# income multiplier GDP,0.5+(0.5*x);TaxEvasion,1.0-(0.2*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'TAX75'
		self.value = 0.75
		
		# connections:
		self.effects.append(SimulationConnection('socialist', '0.0 + (0.112 * x)'))
		self.effects.append(SimulationConnection('capitalist', '0.0 - (0.33 * x)'))
		self.effects.append(SimulationConnection('equality', '0.0 + (0.3 * x)', 4))
		self.effects.append(SimulationConnection('middleIncome_mood', '0.0 - (1.07 * x)'))
		self.effects.append(SimulationConnection('wealthy_mood', '0.0 - (x ** 11)'))
		self.effects.append(SimulationConnection('_low_income', '0.0 - (0.10 * x)'))
		self.effects.append(SimulationConnection('_middle_income', '0.0 - (0.14 * x)'))
		self.effects.append(SimulationConnection('_high_income', '0.0 - (0.20 * x)'))

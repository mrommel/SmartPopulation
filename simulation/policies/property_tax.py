"""
	property tax policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class PropertyTaxPolicy(PolicyBase):
	"""
		property tax policy
	"""
	
	def __init__(self):
		super().__init__(
			"Property Tax",
			"Property tax is a tax levied on the value of homes. The valuation is often made by a government body, "
			"and the money is used to fund local government services (at least in part) such as the provision of "
			"street lighting and emergency services. Some see it as a fair tax which mostly affects those who own "
			"large homes and are wealthy, others see it as an unfair tax on retired people with large homes but little "
			"actual income.",
			category=SimulationCategory.tax,
			slider=[
				'TAX0', 'TAX5', 'TAX10', 'TAX15', 'TAX20', 'TAX25', 'TAX30', 'TAX35', 'TAX40', 'TAX45', 'TAX50',
				'TAX55', 'TAX60', 'TAX65', 'TAX70', 'TAX75', 'TAX80', 'TAX85', 'TAX90', 'TAX95', 'TAX100'
			],
			can_be_cancelled=True,
			introduce=37,  # in political capital
			cancel=33,  # in political capital
			raise_cost=19,  # in political capital
			lower_cost=10,  # in political capital
			min_cost=0,
			max_cost=0,
			implementation=2,
			min_income=1150,
			max_income=12650
		)
		
		self.cost_multiplier = []  # none for taxes
		# income multiplier GDP,0.5+(0.5*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'TAX75'
		self.value = 0.75
		
		# connections:
		self.effects.append(SimulationConnection('_middle_income', '0.0 - (0.1 * x)'))
		self.effects.append(SimulationConnection('_high_income', '0.0 - (0.14 * x)'))
		self.effects.append(SimulationConnection('socialist_mood', '0.0 + (0.12 * x)'))
		self.effects.append(SimulationConnection('capitalist_mood', '0.0 - (0.15 * x)'))
		self.effects.append(SimulationConnection('equality', '0.0 + (0.15 * x)'))
		self.effects.append(SimulationConnection('middle_income_mood', '0.0 - (0.32 * x)'))
		self.effects.append(SimulationConnection('wealthy_mood', '0.0 - (x ** 11)'))
		self.effects.append(SimulationConnection('retired_mood', '0.0 - (0.28 * x)'))
	
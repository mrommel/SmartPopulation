"""
	sales tax policy
"""
from simulation.base import SimulationCategory, PolicyBase, SimulationConnection, SimulationEmotion


class SalesTaxPolicy(PolicyBase):
	"""
		sales tax policy
	"""
	
	def __init__(self):
		super().__init__(
			"Sales Tax",
			"Sales tax is the classic 'regressive' tax, which means it does not take into account the ability to pay. "
			"Critics argue that this affects the poor disproportionately and thus increases inequality. Supporters "
			"argue that it is relatively easy to collect and affects everyone, and is thus fair. Businesses can be "
			"opposed to the administrative burden of the tax.",
			category=SimulationCategory.tax,
			slider=[
				'TAX0', 'TAX5', 'TAX10', 'TAX15', 'TAX20', 'TAX25', 'TAX30', 'TAX35', 'TAX40', 'TAX45', 'TAX50',
				'TAX55', 'TAX60', 'TAX65', 'TAX70', 'TAX75', 'TAX80', 'TAX85', 'TAX90', 'TAX95', 'TAX100'
			],
			can_be_cancelled=True,
			introduce=37,  # in political capital
			cancel=21,  # in political capital
			raise_cost=26,  # in political capital
			lower_cost=9,  # in political capital
			min_cost=0,
			max_cost=0,
			implementation=1,
			min_income=575,
			max_income=61732
		)
		
		self.cost_multiplier = []  # none for taxes
		# income multiplier GDP,0.2+(0.8*x);TaxEvasion,1.0-(0.2*x)
		
		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'TAX75'
		self.value = 0.75
		
		# connections:
		self.effects.append(SimulationConnection('poverty_rate', '0.00 + (0.20 * x)'))
		self.effects.append(SimulationConnection('self_employed_mood', '0.00 - (0.21 * x)'))
		self.effects.append(SimulationConnection('capitalist_mood', '0.00 - (0.15 * x)'))
		self.effects.append(SimulationConnection('equality', '-0.02 - (0.32 * x)'))
		self.effects.append(SimulationConnection('_low_income', '0.0 - (0.12 * x)'))
		self.effects.append(SimulationConnection('_middle_income', '0.0 - (0.06 * x)'))
		
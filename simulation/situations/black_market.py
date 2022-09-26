"""
	situation of black market
"""
from simulation.base import SituationBase, SimulationCategory, SimulationConnection


class BlackMarketSituation(SituationBase):
	"""
		situation of black market
	"""
	
	def __init__(self):
		super().__init__(
			'Black Market',
			'Every economy has a black market, but the situation has started to get out of control. People are '
			'increasingly working for cash in order to dodge paying income and corporation tax, and people who are '
			'claiming state benefits are also working and not declaring the income. This may be a sign that the '
			'citizens consider themselves over taxed and not sufficiently supported by the state.',
			'Fraud experts at the tax office tell you that we have a significant \'black market\' with people avoiding '
			'paying the correct amount of tax',
			'Official tax department reports indicate a significant drop in the size of the \'black market\' of '
			'untaxed work. A smaller black market will have a beneficial knock-on effect on the crime rate.',
			SimulationCategory.tax,
			0.4,  # default
			0.5,
			0.4
		)
		
		# input @todo
		# corporation_tax,0+(0.3*x),4	# black_market
		
		# effects
		self.effects.append(SimulationConnection('crime_rate', '0.05 + (0.05 * x)'))
		# income_tax_income, 1.0 - (0.03 * x)
		# salesTax_income, 1.0 - (0.03 * x)
		# corporationTax_income, 1.0 - (0.03 * x)



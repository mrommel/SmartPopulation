"""
	situation of tax evasion
"""
from simulation.base import SituationBase, SimulationCategory, Effect


class TaxEvasionSituation(SituationBase):
	"""
		situation of tax evasion
	"""
	
	def __init__(self):
		super().__init__(
			'Tax Evasion',
			'There is always a small section of society determined to avoid paying their fair share of taxes, '
			'but tax evasion has turned into an epidemic, with inspectors unable to cope with the number of scams and '
			'evaders.',
			'Tax inspectors report a surge in tax evasion with large sums of money going unpaid.',
			'The level of tax evasion in the economy has declined back to acceptable levels. This is great news '
			'because we will take more money in from taxes without the negative political effects of raising the '
			'levels.',
			SimulationCategory.tax,
			0.3,  # default
			0.6,
			0.4
		)
		
		# input @todo move to each simulation inputs
		# CorporationTax,0.3*(x^2),4	# tax_evasion
		# CapitalGainsTax,0.12*(x^2),4		# tax_evasion
		# FlatTax,0.6*(x^4),4		# tax_evasion
		
		# effects
		# self.effects.append(Effect('', ''))
	
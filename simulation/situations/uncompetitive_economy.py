"""
	situation of uncompetitive economy
"""
from simulation.base import SituationBase, SimulationCategory, Effect


class UncompetitiveEconomySituation(SituationBase):
	"""
		situation of uncompetitive economy
	"""
	
	def __init__(self):
		super().__init__(
			'Uncompetitive Economy',
			'Our workers lack of relative productivity and competitiveness is causing our exports to fall and flooding '
			'our country with cheap imports made overseas, with lower wages, harder working and more technologically '
			'savvy employees. This is having a negative effect on our economy, as our local companies cannot compete '
			'globally.',
			'Economic advisors are concerned by the lack of competitiveness of our companies in global markets.',
			'The earlier problems of a lack of competitiveness by our companies has now subsided.',
			SimulationCategory.economy,
			0.8,  # default
			0.6,
			0.4
		)
		
		# input @todo move to each simulation inputs
		# CorporationTax,0+(0.3*x)		# uncompetitive_economy
		# ImportTarrifs,-0.1-(0.3*x)	# uncompetitive_economy
		
		# effects
		self.effects.append(Effect('gdp', '0.0 - (0.34 * x) ** 1.52'))
		self.effects.append(Effect('capitalist_mood', '-0.04 - (0.06 * x)'))

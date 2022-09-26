"""
	situation of organised crime
"""
from simulation.base import SituationBase, SimulationCategory, SimulationConnection


class OrganisedCrimeSituation(SituationBase):
	"""
		situation of organised crime
	"""
	
	def __init__(self):
		super().__init__(
			'Organised Crime',
			'Large organized gangs of serious criminals are now targeting our country. We do not have the resources to '
			'deal with them, and they are causing serious problems including higher levels of street crime and violent '
			'crime, as well as supplying drugs and guns.',
			'The serious crime dept. has reported that we now have a major problem with organized crime.',
			'The police have now cracked the problem with organized crime, and the crime lords are now behind bars.',
			SimulationCategory.law_and_order,
			0.75,
			0.6,
			0.4
		)

		# input @todo move to each simulation inputs
		# IDCards,0-(0.1*x)
		# IntelligenceServices,0-(0.3*x)
		# PhoneTapping,0-(0.24*x)
		# Gambling,0+(0.45*x)
		# ArmedPolice,0-(0.17*x)
		# Narcotics,0-(0.15*x)
		# PoliceDrones,-0.1-(0.05*x)
		# LegaliseProstitution,-0.05-(0.1*x)

		# effects
		self.effects.append(SimulationConnection('crime_rate', '0.1 + (0.2 * x)'))
		self.effects.append(SimulationConnection('violent_crime_rate', '0 + (0.2 * x)'))

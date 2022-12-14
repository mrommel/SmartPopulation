"""
	situation of homelessness
"""
from simulation.base import SituationBase, SimulationCategory, Effect


class HomelessnessSituation(SituationBase):
	"""
		situation of homelessness
	"""
	
	def __init__(self):
		super().__init__(
			'Homelessness',
			'More and more of our citizens are homeless and have taken to sleeping in the streets. This is having '
			'knock-on effects in the areas of crime and violent crime, and is also reducing everyone\'s quality of '
			'life. Something needs to be done to provide homes for these people!',
			'We now have a homelessness problem. Many of our cities have people sleeping in the streets, often begging '
			'for money.',
			'We no longer have a problem with homelessness and people sleeping on our streets. This will cheer up our '
			'more liberal citizens, socialists, and of course the poorer members of our society.',
			SimulationCategory.welfare,
			0.1,  # default
			0.6,
			0.4
		)
		
		# input @todo
		# homelessness-UnemployedBenefit,0-(0.3*x)
		# homelessness-MortgageTaxRelief,-0.04-(0.04*x)
	
		# effects
		self.effects.append(Effect('liberal_mood', '-0.09 - (0.09 * x)'))
		self.effects.append(Effect('poor_mood', '-0.24 - (0.3 * x)'))
		self.effects.append(Effect('middle_income_mood', '-0.06 - (0.05 * x)'))
		self.effects.append(Effect('crime_rate', '0.04 + (0.04 * x)'))
		self.effects.append(Effect('street_gangs', '0.0 + (0.1 * x)', 2))
		
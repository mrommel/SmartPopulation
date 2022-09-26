"""
	situation of homelessness
"""
from simulation.base import SituationBase, SimulationCategory, SimulationConnection


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
		# StateHousing,0-(0.4*x)	 homelessness
		# PrivateHousing,0-(0.4*x)	homelessness
		# UnemployedBenefit,0-(0.3*x)	homelessness
		# MortgageTaxRelief,-0.04-(0.04*x)	homelessness
		# PropertyTax,0+(0.04*x)	homelessness
	
		# effects
		self.effects.append(SimulationConnection('liberal_mood', '-0.09 - (0.09 * x)'))
		self.effects.append(SimulationConnection('poor_mood', '-0.24 - (0.3 * x)'))
		self.effects.append(SimulationConnection('middle_income_mood', '-0.06 - (0.05 * x)'))
		self.effects.append(SimulationConnection('crime_rate', '0.04 + (0.04 * x)'))
		
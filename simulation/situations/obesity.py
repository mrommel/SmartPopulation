"""
	situation of obesity
"""
from simulation.base import SituationBase, SimulationCategory, SimulationConnection


class ObesitySituation(SituationBase):
	"""
		situation of obesity
	"""
	
	def __init__(self):
		super().__init__(
			'Obesity',
			'Too many of our citizens are eating badly, possibly due to an abundance of junk food at cheap prices. '
			'This will have knock on effects for lifespan and for healthcare costs.	',
			'There is a worrying trend of obesity amongst our citizens, which will shorten peoples lifespan and '
			'increase health costs.',
			'We are happy to report that the obesity problem now seems to be under control.	',
			SimulationCategory.public_services,
			0.3,
			0.6,
			0.4
		)
		
		# input @todo move to each simulation
		# AgricultureSubsidies,0.1+(0.32*x),8 # obesity
		# StateHealthService,-0.2*(x^6),12 # obesity
		# PrivateHealthcare,-0.2*(x^6),12 # obesity
		# JunkFoodTax,-0.16-(0.15*x),10 # obesity
		# OrganicSubsidy,-0.05-(0.072*x),8 # obesity
		# HealthFoodSubsidies,-0.12-(0.14*x),9 # obesity

		# effect connections
		self.effects.append(SimulationConnection('health', '0 - (0.16 * x)'))
		# state_health_service_cost,0.05+(0.15*x),6
		# HealthTaxCredits_cost,0.05+(0.15*x),6
		# HealthcareVouchers_cost,0.05+(0.15*x),6


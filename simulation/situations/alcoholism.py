"""
	situation of alcoholism
"""
from simulation.base import SituationBase, SimulationCategory, SimulationConnection


class AlcoholismSituation(SituationBase):
	"""
		situation of alcoholism
	"""
	
	def __init__(self):
		super().__init__(
			'Alcohol Abuse',
			'We have a serious problem with people consuming alcohol in large quantities. This is obviously bad for '
			'their health but its also leading to crime and disorder in our cities.	',
			'A new problem of \'Alcohol Abuse\' where our citizens consume unhealthy amounts of alcohol has started to '
			'cause problems on our streets.	',
			'The phenomena of \'Alcohol Abuse\' has apparently subsided.	',
			SimulationCategory.law_and_order,
			0.4,  # default
			0.6,
			0.4
		)
		
		# input @todo
		# CCTVCameras,-0.1-(0.1*x) alcoholism
		# DeathPenalty,-0.1-(0.05*x) alcoholism
	
		# effects
		self.effects.append(SimulationConnection('conservatives_mood', '-0.2 - (0.3 * x)'))
		self.effects.append(SimulationConnection('conservatives_freq', '0.04 + (0.04 * x)', 2))
		self.effects.append(SimulationConnection('tourism', '-0.08 - (0.05 * x)'))

"""
	situation of street gangs
"""
from simulation.base import SituationBase, SimulationCategory, Effect


class StreetGangsSituation(SituationBase):
	"""
		situation of street gangs
	"""
	
	def __init__(self):
		super().__init__(
			'Street Gangs',
			'Street gangs are an ever more common sight on the streets of our cities. Although not all street gangs '
			'are involved in violence, some are, and there must be something that our teenage citizens could be doing '
			'rather than loitering on street corners?',
			'Police chiefs report a significant new problem in terms of street gangs, often related to violent crime.',
			'At a recent press conference, our Chief of Police was happy to report that the earlier problem of '
			'\'street gangs\' is now under control, which means less crime, and happier citizens.',
			SimulationCategory.law_and_order,
			0.0,  # default
			0.6,
			0.4
		)
		
		# input @todo move to each simulation inputs
		# CCTVCameras,-0.05-(0.05*x)	# street_gangs
		# CommunityPolicing,-0.05-(0.1*x),4	# street_gangs
		# PoliceDrones,-0.1-(0.1*x)	# street_gangs
		
		# effects
		self.effects.append(Effect('crime_rate', '0.12 + (0.1 * x)'))
		self.effects.append(Effect('conservatives_mood', '-0.1 - (0.1 * x)'))
		self.effects.append(Effect('retired_mood', '-0.1 - (0.2 * x)'))
		# _self.effects.append(Effect('global_liberalism', '-0.06 - (0.03 * x)'))
		self.effects.append(Effect('all_mood', '-0.05 - (0.05 * x)'))

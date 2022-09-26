"""poverty simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class PovertySimulation(SimulationBase):
	"""
		poverty simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Poverty",
			"One of the most widely used measures of comparison between nations. The poverty level is periodically "
			"reassessed, but all nations should strive to get their poverty rate as low as possible.",
			SimulationCategory.welfare,
			0.64,
			emotion=SimulationEmotion.high_bad
		)
		
		# connections:
		self.effects.append(SimulationConnection('poor_mood', '0.3 - (x ** 2)'))
		self.effects.append(SimulationConnection('crime_rate', '0.41 * (x ** 2.0)', 4))
		self.effects.append(SimulationConnection('racial_tension', '0 + (0.22 * x)', 2))
		# _global_socialism,0.2*(x^5)
		self.effects.append(SimulationConnection('socialist_mood', '-0.35 * (x ** 2)'))
		self.effects.append(SimulationConnection('homelessness', '0.0 + (0.9 * x)'))

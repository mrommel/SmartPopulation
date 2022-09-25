"""crime rate simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class CrimeRateSimulation(SimulationBase):
	"""
		crime rate simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Crime",
			"An indicator of the level of general non violent crime in your nation. This includes crimes such as car "
			"crime, burglary etc., but also covers fraud and other similar crimes.",
			SimulationCategory.law_and_order,
			0.55,
			emotion=SimulationEmotion.high_bad
		)

		# connections:
		self.effects.append(SimulationConnection('all_mood', '0 - (0.13 * x)'))
		self.effects.append(SimulationConnection('gdp', '0 - (0.08 * x)'))

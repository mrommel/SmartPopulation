"""equality simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class EqualitySimulation(SimulationBase):
	"""
		equality simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Equality",
			"There are many ways to measure equality. Conservatives talk of equality of opportunity, socialists talk "
			"of equality of outcome. This is just a simple measurement of the distribution of wealth (financial "
			"equality of outcome).",
			SimulationCategory.welfare,
			0.4,
			emotion=SimulationEmotion.high_good
		)

		# connections:
		self.effects.append(SimulationConnection('socialist_mood', '-0.2 + (0.4 * x)'))
		self.effects.append(SimulationConnection('crime_rate', '0.1 - (x * 0.22)'))

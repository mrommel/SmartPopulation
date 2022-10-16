"""private housing simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class PrivateHousingSimulation(SimulationBase):
	"""
		private housing simulation
	"""

	def __init__(self):
		super().__init__(
			"Private Housing",
			"The size of the private housing sector. Private housing will respond naturally to supply and demand, "
			"but can be artificially deflated by the supply of subsidized state housing, or rent controls on the "
			"private sector.",
			SimulationCategory.welfare,
			'simulation_default.png',
			0.5,
			emotion=SimulationEmotion.high_bad
		)

		# connections:
		self.effects.append(Effect('_middle_income', '0.0 - (0.08 * x)'))
		self.effects.append(Effect('capitalist', '0.0 + (0.1 * x)'))
		self.effects.append(Effect('homelessness', '0.0 - (0.4 * x)'))

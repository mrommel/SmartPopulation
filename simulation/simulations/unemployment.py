"""unemployment simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class UnemploymentSimulation(SimulationBase):
	"""
		unemployment simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Unemployment",
			"At its simplest this is a count of the percentage of your population who aren't in gainful employment. "
			"Adjusted to omit those citizens who are not actively seeking work for one reason or another.",
			SimulationCategory.economy,
			'simulation_default.png',
			0.4,
			emotion=SimulationEmotion.high_bad
		)
		
		# connections:
		self.effects.append(SimulationConnection('working_week', '0+(0.2*x)'))
		self.effects.append(SimulationConnection('trade_unionist_mood', '0.0 - (0.21 * x)'))
		self.effects.append(SimulationConnection('commuter_freq', '0.0 - (0.28 * x)'))
		self.effects.append(SimulationConnection('socialist_mood', '-0.2 * (x ** 4)'))
		self.effects.append(SimulationConnection('racial_tension', '0.7 * (x ** 3)', 2))
		self.effects.append(SimulationConnection('poverty_rate', '0.24 * (x ** 8)'))
		self.effects.append(SimulationConnection('crime_rate', '0.17 * (x ** 5)'))
		self.effects.append(SimulationConnection('worker_productivity', '-0.215 + (x * 0.3)'))
		self.effects.append(SimulationConnection('wages', '0.2 - (0.4 * x)'))
		self.effects.append(SimulationConnection('poor_mood', '-0.10 * (x ** 2)'))
		self.effects.append(SimulationConnection('immigration', '-0.2 * (x ** 2) + 0.05'))
		self.effects.append(SimulationConnection('obesity', '0.0 + (0.06 * x)', 4))
		self.effects.append(SimulationConnection('homelessness', '0.0 + (0.9 * x)'))
		self.effects.append(SimulationConnection('street_gangs', '0.1 + (0.6 * x)'))
	
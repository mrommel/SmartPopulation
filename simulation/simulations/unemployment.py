"""unemployment simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


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
			'simulation_unemployment.png',
			0.4,
			emotion=SimulationEmotion.high_bad
		)
		
		# connections:
		self.effects.append(Effect('working_week', '0+(0.2*x)'))
		self.effects.append(Effect('trade_unionist_mood', '0.0 - (0.21 * x)'))
		self.effects.append(Effect('commuter_freq', '0.0 - (0.28 * x)'))
		self.effects.append(Effect('socialist_mood', '-0.2 * (x ** 4)'))
		self.effects.append(Effect('racial_tension', '0.7 * (x ** 3)', 2))
		self.effects.append(Effect('poverty_rate', '0.24 * (x ** 8)'))
		self.effects.append(Effect('crime_rate', '0.17 * (x ** 5)'))
		self.effects.append(Effect('worker_productivity', '-0.215 + (x * 0.3)'))
		self.effects.append(Effect('wages', '0.2 - (0.4 * x)'))
		self.effects.append(Effect('poor_mood', '-0.10 * (x ** 2)'))
		self.effects.append(Effect('immigration', '-0.2 * (x ** 2) + 0.05'))
		self.effects.append(Effect('obesity', '0.0 + (0.06 * x)', 4))
		self.effects.append(Effect('homelessness', '0.0 + (0.9 * x)'))
		self.effects.append(Effect('street_gangs', '0.1 + (0.6 * x)'))
	
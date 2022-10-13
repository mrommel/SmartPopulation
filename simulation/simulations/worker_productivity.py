"""worker productivity simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class WorkerProductivitySimulation(SimulationBase):
	"""
		worker productivity simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Productivity",
			"The average output in financial terms of a typical citizen. Some nations have more productive employees "
			"than others, due to such factors as work ethic, technical knowledge and workplace hours.",
			SimulationCategory.economy,
			'simulation_productivity.png',
			0.5,
			emotion=SimulationEmotion.high_good
		)

		# connections:
		self.effects.append(Effect('gdp', '-0.22 + (x * 0.44)'))
		self.effects.append(Effect('international_trade', '-0.2 + (0.4 * x)', 4))
		self.effects.append(Effect('unemployment', '-0.08 + (0.16 * x)', 2))
		self.effects.append(Effect('uncompetitive_economy', '0.0 - (0.7 * x)'))
		self.effects.append(Effect('high_productivity', '0.95 * (x ** 2)'))

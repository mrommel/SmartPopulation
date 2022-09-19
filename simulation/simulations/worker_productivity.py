"""worker productivity simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


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
			0.5
		)

		# connections:
		self.effects.append(SimulationConnection('gdp', '-0.22 + (x * 0.44)'))
		self.effects.append(SimulationConnection('international_trade', '-0.2 + (0.4 * x)', 4))
		self.effects.append(SimulationConnection('unemployment', '-0.08 + (0.16 * x)', 2))

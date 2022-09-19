"""wages simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


class WagesSimulation(SimulationBase):
	"""
		wages simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Wages",
			"The average wage level in your country. Wages are generally set by supply and demand, which roughly "
			"equates to the labor supply and the state of the economy (GDP). Immigration raises the labor supply, "
			"reducing wages, and high unemployment will also put downward pressure on wages. Labor laws, including "
			"minimum wages can push wages artificially higher, although this will have side-effects.",
			SimulationCategory.economy,
			0.5
		)
		
		# connections:
		self.effects.append(SimulationConnection('_low_income', '-0.5 + (1.0 * x)'))
		self.effects.append(SimulationConnection('_middle_income', '-0.3 + (0.6 * x)'))
		self.effects.append(SimulationConnection('worker_productivity', '0.2 - (0.4 * x)'))

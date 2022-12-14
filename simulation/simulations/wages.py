"""wages simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


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
			'simulation_wages.png',
			0.5,
			emotion=SimulationEmotion.high_good
		)
		
		# connections:
		self.effects.append(Effect('_low_income', '-0.5 + (1.0 * x)'))
		self.effects.append(Effect('_middle_income', '-0.3 + (0.6 * x)'))
		self.effects.append(Effect('worker_productivity', '0.2 - (0.4 * x)'))

"""violent crime rate simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class ViolentCrimeRateSimulation(SimulationBase):
	"""
		violent crime rate simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Violent Crime",
			"A more worrying indicator than the overall crime level, this measures the frequency of violent crimes "
			"such as murder, rape and muggings. Violent crime is a worry for everyone in the country.",
			SimulationCategory.law_and_order,
			'simulation_violent_crime_rate.png',
			0.57,
			emotion=SimulationEmotion.high_bad
		)

		# connections:
		self.effects.append(Effect('all_mood', '0 - (0.16 * x)'))
		self.effects.append(Effect('retired_mood', '0 - (0.18 * x)'))
		# _global_liberalism,0.05-(0.1*x)
		self.effects.append(Effect('tourism', '0 -(0.2 * x)', 8))
		self.effects.append(Effect('lifespan', '0.0 - (0.2 * x)'))
	
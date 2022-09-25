"""racial tension simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class RacialTensionSimulation(SimulationBase):
	"""
		racial tension simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Racial Tension",
			"The degree to which there is unease between different nationalities and cultures. Sudden, uncontrolled "
			"immigration can sometimes lead to racial tensions, which can in the worst case, result in violent "
			"clashes.",
			SimulationCategory.foreign_policy,
			0.0,
			emotion=SimulationEmotion.high_bad
		)
		
		# connections:
		self.effects.append(SimulationConnection('violent_crime_rate', '0.45 * (x ** 6)'))
		self.effects.append(SimulationConnection('_terrorism', '-0.2 + (x ** 4)'))
		self.effects.append(SimulationConnection('patriot_freq', '-0.12 + (0.24 * x)'))
		# liberal_freq,0.1-(0.2*x)
		# ethnic_minorities_mood,0-(0.4*x)

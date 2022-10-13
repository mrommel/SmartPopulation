"""technology simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class TechnologySimulation(SimulationBase):
	"""
		technology simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Technology",
			"A general index of the level of technological sophistication of the country, including the percentage of "
			"citizens with internet access, and high speed broadband, as well as the technological understanding of "
			"students, and the capabilities of industry. A high technological index boosts international "
			"competitiveness. Tax incentives may be required to attract high tech industry. ",
			SimulationCategory.economy,
			'simulation_technology.png',
			0.5,
			emotion=SimulationEmotion.high_good
		)

		# connections:
		self.effects.append(Effect('worker_productivity', '0.15 * (x ** 4)'))
		self.effects.append(Effect('education', '-0.1 + (0.16 * x)'))
		self.effects.append(Effect('unemployment', '0.2 * (x ** 8.0)', 2))
		self.effects.append(Effect('retired_freq', '0.10 * (x ** 4.0)', 16))
		self.effects.append(Effect('skills_shortage', '0.25 * (x ** 2)'))
		self.effects.append(Effect('lifespan', '0.0 + (0.15 * x)', 8))

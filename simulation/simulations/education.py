"""education simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class EducationSimulation(SimulationBase):
	"""
		education simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Education",
			"A measurement of the education level of the average citizen. Not only literacy, but numeracy and general "
			"understanding of everything from history to IT and science.",
			SimulationCategory.public_services,
			'simulation_education.png',
			0.18,
			emotion=SimulationEmotion.high_good
		)

		# connections:
		self.effects.append(SimulationConnection('worker_productivity', '-0.2 + (x * 0.4)'))
		self.effects.append(SimulationConnection('racial_tension', '0 - (0.08 * x)'))
		self.effects.append(SimulationConnection('crime_rate', '-0.12 * (x ** 6.0)'))
		self.effects.append(SimulationConnection('violent_crime_rate', '-0.12 * (x ** 4.0)'))
		self.effects.append(SimulationConnection('skills_shortage', '0.0 - (0.4 * x)'))

"""terrorism simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationEmotion


class TerrorismSimulation(SimulationBase):
	"""
		terrorism simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Terrorism",
			"hidden",
			SimulationCategory.hidden,
			'simulation_default.png',
			0.5,
			emotion=SimulationEmotion.high_bad
		)
		
		# input
		# _year,0+(0.01*x)
		
		# connections:
		# self.effects.append(SimulationConnection('???', '???'))

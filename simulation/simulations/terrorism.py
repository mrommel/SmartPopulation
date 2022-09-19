"""terrorism simulation"""
from simulation.base import SimulationCategory, SimulationBase


class TerrorismSimulation(SimulationBase):
	"""
		terrorism simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Terrorism",
			"hidden",
			SimulationCategory.hidden,
			0.5
		)
		
		# input
		# _year,0+(0.01*x)
		
		# connections:
		# self.effects.append(SimulationConnection('???', '???'))

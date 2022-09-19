"""bus usage simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


class BusUsageSimulation(SimulationBase):
	"""
		bus usage simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Bus Usage",
			"A measure of the amount of journeys that are taken by bus, as opposed to car, air or rail. Buses are more "
			"environmentally friendly than cars, so are seen as a way to reduce pollution, as well as reduce traffic "
			"congestion.",
			SimulationCategory.transport,
			0.15
		)
		
		# input @todo
		# GDP,0+(0.1 * x)
		
		# connections:
		self.effects.append(SimulationConnection('car_usage', '0.0 - (0.35 * x)'))
		self.effects.append(SimulationConnection('rail_usage', '0.0 - (0.28 * x)'))
		self.effects.append(SimulationConnection('oil_demand', '0.0 + (0.13 * x)'))

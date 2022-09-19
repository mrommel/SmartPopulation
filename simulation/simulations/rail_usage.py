"""rail usage simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


class RailUsageSimulation(SimulationBase):
	"""
		rail usage simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Rail Usage",
			"A measure of the amount of journeys that take place by rail. Supporters of public transport will look for "
			"high rail usage, in order to reduce both traffic congestion and also pollution. Rail travel can be very "
			"efficient in highly populated countries, but improvements to rail  infrastructure can be extremely "
			"expensive and take a long time.",
			SimulationCategory.transport,
			0.25
		)
		
		# input @todo
		# GDP,0+(0.1 * x)
		
		# connections:
		self.effects.append(SimulationConnection('car_usage', '0.0 - (0.35 * x)'))
		self.effects.append(SimulationConnection('bus_usage', '0.0 - (0.25 * x)'))
		self.effects.append(SimulationConnection('oil_demand', '0.0 + (0.12 * x)'))

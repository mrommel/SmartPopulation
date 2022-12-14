"""rail usage simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


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
			'simulation_rail_usage.png',
			0.25,
			emotion=SimulationEmotion.high_good
		)

		# connections:
		self.effects.append(Effect('car_usage', '0.0 - (0.35 * x)'))
		self.effects.append(Effect('bus_usage', '0.0 - (0.25 * x)'))
		self.effects.append(Effect('oil_demand', '0.0 + (0.12 * x)'))

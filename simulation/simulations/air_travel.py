"""
	air travel simulation
"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class AirTravelSimulation(SimulationBase):
	"""
		air travel simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Air Travel",
			"Air travel is often strongly linked to a country's economy, and thus GDP. Wealthier citizens take more "
			"foreign holidays, and a richer economy will mean more business air travel, and more products shipped by "
			"air freight. The amount of air travel is very price sensitive, so changes in fuel costs, taxes and other "
			"charges can have a major effect.",
			SimulationCategory.transport,
			'simulation_air_travel.png',
			0.0,
			emotion=SimulationEmotion.unknown
		)

		# connections:
		self.effects.append(Effect('co2_emissions', '0.32 * (x ** 2)'))
		self.effects.append(Effect('oil_demand', '0.0 + (0.1 * x)'))
		self.effects.append(Effect('environment', '-0.14 * (x ** 3)'))
		self.effects.append(Effect('rail_usage', '0.0 - (0.04 * x)'))
	
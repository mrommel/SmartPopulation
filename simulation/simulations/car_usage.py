"""car usage simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class CarUsageSimulation(SimulationBase):
	"""
		car usage simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Car Usage",
			"A measure of how many miles per year the average household travels by car. High car usage can cause "
			"pollution, but is inevitable in a booming economy with poor provision of public transport.",
			SimulationCategory.transport,
			'simulation_car_usage.png',
			0.6,
			emotion=SimulationEmotion.high_good
		)
		
		# connections:
		self.effects.append(Effect('environment', '0.0 - (0.22 * x)'))
		self.effects.append(Effect('motorist_freq', '-0.4 + (0.8 * x)'))
		self.effects.append(Effect('co2_emissions', '0.0 - (0.5 * x)'))
		self.effects.append(Effect('oil_demand', '0.0 + (0.3 * x)'))
	
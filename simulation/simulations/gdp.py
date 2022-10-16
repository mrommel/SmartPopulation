"""gdp simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class GDPSimulation(SimulationBase):
	"""
		gdp simulation
	"""

	def __init__(self):
		super().__init__(
			"GDP",
			"The Gross Domestic product of your country. This is defined as The total market value of all the goods "
			"and services produced within the nation in a year. This is a good general-purpose measure of the strength "
			"of your economy, and the nations overall wealth. One of the contributing factors is the global economic "
			"cycle, which tends to be cyclical, and is beyond your control.",
			SimulationCategory.economy,
			'simulation_gdp.png',
			0.35,
			emotion=SimulationEmotion.high_good
		)

		# connections:
		self.effects.append(Effect('capitalist_mood', '-0.2 + (0.65 * x)'))
		self.effects.append(Effect('co2_emissions', '0.0 + (0.6 * x)'))
		self.effects.append(Effect('air_travel', '0.0 + (1.0 * x)'))
		self.effects.append(Effect('immigration', '0.98 * (x ** 4)', 4))
		self.effects.append(Effect('unemployment', '0.9 - (0.7 * x)'))
		self.effects.append(Effect('environment', '-0.84 * (x ** 2)'))
		self.effects.append(Effect('equality', '-0.15 * (x ** 4)'))
		self.effects.append(Effect('oil_demand', '0.0 + (0.4 * x)'))
		self.effects.append(Effect('obesity', '0 + (0.45 * x)', 8))
		self.effects.append(Effect('rail_usage', '0 + (0.1 * x)'))
		self.effects.append(Effect('car_usage', '0 + (0.4 * x)'))
		self.effects.append(Effect('bus_usage', '0 + (0.1 * x)'))
		self.effects.append(Effect('private_healthcare', '0.0 + (0.4 * x)', 4))
		self.effects.append(Effect('private_housing', '0.0 + (0.5 * x)', 4))
		self.effects.append(Effect('private_schools', '0.0 + (0.5 * x)', 4))

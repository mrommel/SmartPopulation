"""international trade simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class InternationalTradeSimulation(SimulationBase):
	"""
		international trade simulation
	"""
	
	def __init__(self):
		super().__init__(
			"International Trade",
			"International trade is generally good for an economy, due to the law of comparative advantage, "
			"effectively helping each country to produce what it is best at. Trade can be restricted by political "
			"problems with other countries, where arguments can lead to import tariffs and sanctions. In some cases, "
			"countries also indulge in 'protectionism' to defend politically sensitive industries against foreign "
			"competition.",
			SimulationCategory.foreign_policy,
			'simulation_international_trade.png',
			1.0,
			emotion=SimulationEmotion.high_good
		)
		
		# connections:
		self.effects.append(SimulationConnection('gdp', '0 + (0.15 * x)'))
		self.effects.append(SimulationConnection('air_travel', '0 + (0.2 * x)'))

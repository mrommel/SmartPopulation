"""low income simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


class LowIncomeSimulation(SimulationBase):
	"""
		low income simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Poor Earnings",
			"The effective income of those people who are on low (or no) earnings in our society. If this value rises "
			"high enough (through benefits and tax exemptions for the poor), then more people will move out of poverty "
			"and in to the middle income group. Progressive taxation, combined with well-funded public services and "
			"state benefits are the most popular ways to 'lift people' out of poverty.",
			SimulationCategory.economy,
			0.0,
			-1.0,
			1.0
		)

		# connections:
		self.effects.append(SimulationConnection('car_usage', '0.1 * (x ** 3.0)'))
		self.effects.append(SimulationConnection('bus_usage', '0.0 - (0.05 * x)'))
		self.effects.append(SimulationConnection('air_travel', '0.1 * (x ** 4.0)'))
		
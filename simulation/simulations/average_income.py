"""average income simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationEmotion


class AverageIncomeSimulation(SimulationBase):
	"""
		average income simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Average Income",
			"A simple measurement of the average wage or income for your citizens. This statistic can be misleading "
			"because of the effect of inequality, the average income may be very different to the income of most of "
			"your citizens in an unequal society",
			SimulationCategory.economy,
			0.50,
			emotion=SimulationEmotion.high_good
		)

		# connections:

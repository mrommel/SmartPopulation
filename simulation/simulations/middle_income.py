"""middle income simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class MiddleIncomeSimulation(SimulationBase):
	"""
		middle income simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Middle Earnings",
			"The effective income of those people on average earnings, not wealthy or poor. This is generally the "
			"largest group of people in the economy, so policies which affect this value can be big vote deciders. "
			"Middle income earners are expected to own their own homes (or be buying them), and often own one or more "
			"cars. They probably take holidays abroad at least once a year. Taxes that affect any of these will hit "
			"these people hardest, and may push some of them down into poverty",
			SimulationCategory.economy,
			'simulation_middle_income.png',
			0.0,
			-1.0,
			1.0,
			emotion=SimulationEmotion.high_good
		)

		# connections:
		self.effects.append(Effect('car_usage', '0.2 * (x ** 3)'))
		self.effects.append(Effect('air_travel', '0.2 * (x ** 3)'))

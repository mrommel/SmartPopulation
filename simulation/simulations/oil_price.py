"""oil price simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class OilPriceSimulation(SimulationBase):
	"""
		oil price simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Oil Price",
			"The oil price affects the economy, with higher prices lowering our general standard of living, "
			"although this will be mitigated by energy efficiency measures. A lower level of oil dependence will also "
			"make us less sensitive to global oil price shocks caused by political instabilities.",
			SimulationCategory.transport,
			0.1,
			emotion=SimulationEmotion.high_bad
		)
		
		# connections:
		self.effects.append(SimulationConnection('gdp', '0.22 - (0.4 * x)'))
		# Motorist,0.3-(0.6*x),2
		# Motorist_income,0.2-(0.4*x),2
		# Motorist_freq,0.2-(0.4*x),12

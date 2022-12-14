"""oil price simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


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
			'simulation_default.png',
			0.1,
			emotion=SimulationEmotion.high_bad
		)
		
		# connections:
		self.effects.append(Effect('gdp', '0.22 - (0.4 * x)'))
		self.effects.append(Effect('motorist_mood', '0.3 - (0.6 * x)', 2))
		# self.effects.append(Effect('motorist_income,0.2-(0.4*x),2
		self.effects.append(Effect('motorist_freq', '0.2 - (0.4 * x)', 12))

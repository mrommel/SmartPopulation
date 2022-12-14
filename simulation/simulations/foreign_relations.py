"""foreign relations simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class ForeignRelationsSimulation(SimulationBase):
	"""
		foreign relations simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Foreign Relations",
			"Foreign relations are important for two reasons, firstly as a way of preventing disputes escalating into "
			"wars or terrorism which may threaten our citizens, and secondly, as a way to ensure trade relations are "
			"good and that we benefit economically from trade and tourism with other nations.",
			SimulationCategory.foreign_policy,
			'simulation_foreign_relation.png',
			0.14,
			emotion=SimulationEmotion.high_good
		)
		
		# connections:
		self.effects.append(Effect('racial_tension', '0.3 - (0.6 * x)'))
		self.effects.append(Effect('_terrorism', '0.24 - (x * 1)'))
		self.effects.append(Effect('patriot_freq', '0.2 - (0.4 * x)'))
		self.effects.append(Effect('immigration', '-0.1 + (0.2 * x)'))
		self.effects.append(Effect('tourism', '0 + (0.4 * x)', 4))
		self.effects.append(Effect('international_trade', '-0.2 + (0.2 * x)', 4))
		
"""foreign relations simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection


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
			0.14
		)
		
		# connections:
		self.effects.append(SimulationConnection('racial_tension', '0.3 - (0.6 * x)'))
		self.effects.append(SimulationConnection('_terrorism', '0.24 - (x * 1)'))
		self.effects.append(SimulationConnection('patriot_freq', '0.2 - (0.4 * x)'))
		self.effects.append(SimulationConnection('immigration', '-0.1 + (0.2 * x)'))
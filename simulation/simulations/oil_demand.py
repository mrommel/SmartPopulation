"""oil demand simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class OilDemandSimulation(SimulationBase):
	"""
		oil demand simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Oil Demand",
			"Our demand for oil comes from industry, road travel and air travel. The more our citizens fly and drive, "
			"the greater our demand for oil, although energy efficiency measures and hybrid cars can reduce this "
			"somewhat, as can investments in cleaner industry and renewable energy sources.",
			SimulationCategory.transport,
			0.1,
			emotion=SimulationEmotion.high_good
		)
		
		# input @todo
		# _globaleconomy_,-0.1+(0.2*x)
		
		# connections:
		self.effects.append(SimulationConnection('oil_price', '0.0 + (0.5 * x)'))

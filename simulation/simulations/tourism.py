"""tourism simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class TourismSimulation(SimulationBase):
	"""
		tourism simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Tourism",
			"The size of the tourism industry. Tourists will prefer to visit countries with no major social problems, "
			"and also prefer low sales taxes. A decent reputation for your country overseas will also boost tourism. "
			"Generally, tourism is seen as positive as it brings money into the economy. Encouraging tourism may "
			"partially depend on low air travel costs, which can have implications for pollution and CO2 emissions.",
			SimulationCategory.economy,
			0.35,
			emotion=SimulationEmotion.high_good
		)
		
		# input @todo
		# AirlineTax,0-(0.3*x)
		# AntisocialBehaviour,0-(0.1*x)
		# StreetGangs,0-(0.3*x)
		# BorderControls,0.0-(0.22*x)
		# SalesTax,0-(0.05*x)
		# _globaleconomy_,0+(0.25*x)
		# ClassWarfare,0-(0.4*x)
		
		# connections:
		self.effects.append(SimulationConnection('gdp', '0+(0.12*x)'))
		
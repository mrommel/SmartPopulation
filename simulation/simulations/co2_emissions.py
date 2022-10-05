"""CO2 emissions simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class CO2EmissionsSimulation(SimulationBase):
	"""
		CO2 emissions simulation
	"""
	
	def __init__(self):
		super().__init__(
			"CO2 Emissions",
			"Amount of carbon we put into the atmosphere. Environmentalists and the majority of scientists agree that "
			"limiting our CO2 Emissions is a vital step we should take to fight climate change. Failing to control our "
			"emissions can lower our international standing and affect foreign relations. A booming economy, "
			"if unchecked, will produce more carbon, as will high levels of car and air travel. There are a vast range "
			"of different strategies that can be employed to minimize the level of CO2 emissions.",
			SimulationCategory.law_and_order,
			'simulation_co2_emissions.png',
			0.2,
			emotion=SimulationEmotion.high_bad
		)
		
		# connections:
		self.effects.append(SimulationConnection('foreign_relations', '0 - (0.1 * x)'))
		self.effects.append(SimulationConnection('environmentalist_mood', '0.1 + (x ** 2) * -0.7'))

"""energy efficiency simulation"""
from simulation.base import SimulationCategory, SimulationBase, SimulationConnection, SimulationEmotion


class EnergyEfficiencySimulation(SimulationBase):
	"""
		energy efficiency simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Energy Efficiency",
			"This is a general measure of how efficiently the country uses its energy resources. Low car energy "
			"standards, and a lack of investment in new technology will mean a wasteful economy, and in turn, "
			"higher demand for fossil fuels such as oil. Reducing energy usage has become more urgent in recent times "
			"due to concerns about climate change, and the drive to reduce CO2 emissions.",
			SimulationCategory.economy,
			0.5,
			emotion=SimulationEmotion.high_good
		)
		
		# connections:
		self.effects.append(SimulationConnection('gdp', '0.0 + (0.05 * x)'))
		self.effects.append(SimulationConnection('co2_emissions', '0.0 - (0.2 * x)'))
		self.effects.append(SimulationConnection('oil_demand', '0.0 - (0.1 * x)'))

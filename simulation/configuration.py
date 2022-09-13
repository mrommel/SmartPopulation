class SimulationConfiguration:
	"""
	configuration of the simulation
	"""
	
	def __init__(self, life_expectancy: float, number_of_children_per_women: float, boys_ratio: float = 51.4):
		"""
		value constructor
		"""
		self.life_expectancy = life_expectancy  # in years
		self.number_of_children_per_women = number_of_children_per_women
		self.boys_ratio = boys_ratio  # in percent


class SimulationConfigurationGermany2019(SimulationConfiguration):
	
	def __init__(self):
		super().__init__(life_expectancy=81.8, number_of_children_per_women=1.62, boys_ratio=51.4)

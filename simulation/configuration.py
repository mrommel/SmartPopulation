"""simulation configuration module."""


class SimulationConfiguration:
	"""
		configuration of the simulation
	"""
	
	def __init__(self, life_expectancy: float, number_of_children_per_women: float, boys_ratio: float = 51.4):
		"""
			value constructor
			
			:param life_expectancy: average life span expectancy in years
			:param number_of_children_per_women: average number of born children per women
			:param boys_ratio: ratio of boys born in percent (in comparison to girls)
		"""
		self.life_expectancy = life_expectancy  # in years
		self.number_of_children_per_women = number_of_children_per_women
		self.boys_ratio = boys_ratio  # in percent


class SimulationConfigurationGermany2019(SimulationConfiguration):
	"""
		configuration of the simulation for germany in 2019
	"""
	
	def __init__(self):
		"""
			default constructor of a configuration for germany in 2019
		"""
		super().__init__(life_expectancy=81.8, number_of_children_per_women=1.62, boys_ratio=51.4)

""" base types of simulations """

from enum import Enum


class SimulationCategory(Enum):
	"""
		enum that represents simulation categories
	"""
	public_services = 0
	law_and_order = 1
	economy = 2
	foreign_policy = 3
	welfare = 4
	transport = 5
	
	hidden = 10
	people = 20


class SimulationConnection:
	"""
		class that represents a connection between simulations / situations
	"""
	
	def __init__(self, target_name: str, formula: str, inertia: int = 1):
		"""
			value constructor
			
			:param target_name: name of the target variable / simulation / situation
			:param formula: formula
			:param inertia: averages out over the last x values
		"""
		self.target_name = target_name  # name of the target
		self.formula = formula
		self.inertia = inertia
	
	def evaluate(self, value: float):
		"""
			evaluate formula
		
			:param value: x value of formula
			:return: evaluated formula
		"""
		return eval(self.formula, {"x": value})


class SimulationBase:
	"""
		base class of all simulations
	"""
	
	def __init__(
			self,
			name: str,
			description: str,
			category: SimulationCategory,
			default_value: float,
			min_value: float = 0.0,
			max_value: float = 1.0
	):
		"""
			value constructor
		
			:param name: name of the simulation
			:param description: description of the simulation
			:param category: category of the simulation
			:param default_value: default value of the simulation
			:param min_value: minimal value
			:param max_value: maximal value
		"""
		self.name = name
		self.description = description
		self.category = category
		
		# values
		self.default_value = default_value
		self.value = default_value
		self.new_value = default_value
		self.min_value = min_value
		self.max_value = max_value
		
		self.effects = []
		self.history = []
	
	def prepare(self):
		"""
			prepares the values for iteration

			:return: (nothing)
		"""
		self.new_value = 0.0
	
	def iterate(self, simulation):
		"""
			evaluates the values during iteration
		
			:param simulation: simulation that is updated
			:return: (nothing)
		"""
		for effect in self.effects:
			tmp_value = self.value
			tmp_sum = 1.0
			for index in range(0, effect.inertia - 1):
				if index < len(self.history):
					tmp_value += self.history[index]
				else:
					tmp_value += self.value
				tmp_sum += 1.0
			
			tmp_value /= tmp_sum
			
			without_mood = effect.target_name.replace('_mood', '')
			without_freq = effect.target_name.replace('_freq', '')
			
			if effect.target_name in simulation.simulations:
				simulation.simulations[effect.target_name].new_value += effect.evaluate(tmp_value)
			elif effect.target_name in simulation.situations:
				simulation.situations[effect.target_name].new_value += effect.evaluate(tmp_value)
			elif without_mood in simulation.groups:
				simulation.groups[without_mood].mood.new_value += effect.evaluate(tmp_value)
			elif without_freq in simulation.groups:
				simulation.groups[without_freq].freq.new_value += effect.evaluate(tmp_value)
			else:
				raise Exception(f'can\'t get "{effect.target_name}" as simulation value')
	
	def finish(self):
		"""
			post processes values after iteration

			:return: (nothing)
		"""
		self.value = self.default_value + self.new_value
		
		# limit value based on min and max
		if self.value < self.min_value:
			self.value = self.min_value
		
		if self.value > self.max_value:
			self.value = self.max_value
		
		# put to history
		self.history.insert(0, self.value)
	
	def print(self):
		"""
			print the current name and value
		
			:return: (nothing)
		"""
		print(f'{self.name:24}: \t{self.value:.2f}')


class GroupBase:
	"""
		base class of all groups (all, retired, etc)
	"""
	
	def __init__(self, name, description, mood_default_value, freq_default_value):
		"""
			base class of all groups
		
			:param name: name of the group
			:param description: description of the group
			:param mood_default_value: default value of mood (in percent)
			:param freq_default_value: default value of frequency (in percent)
		"""
		self.name = name
		self.description = description
		self.category = SimulationCategory.people
		
		self.mood = SimulationBase(name + '_mood', '', SimulationCategory.people, mood_default_value)
		self.freq = SimulationBase(name + '_freq', '', SimulationCategory.people, freq_default_value)
	
	def prepare(self):
		"""
			prepares the values for iteration
		
			:return: (nothing)
		"""
		self.mood.prepare()
		self.freq.prepare()
	
	def iterate(self, simulation):
		"""
			evaluates the values during iteration

			:param simulation: simulation that is updated
			:return: (nothing)
		"""
		self.mood.iterate(simulation)
		self.freq.iterate(simulation)
	
	def finish(self):
		"""
			post processes values after iteration

			:return: (nothing)
		"""
		self.mood.finish()
		self.freq.finish()
	
	def print(self):
		"""
			print the current name and value

			:return: (nothing)
		"""
		print(f'{self.name:24}: \tfreq={self.freq.value * 100.0:.2f}% / \tmood={self.mood.value}')


class SituationBase:
	"""
		base class for situations
	"""
	
	def __init__(
			self,
			name: str,
			description: str,
			start_text: str,
			end_text: str,
			category: SimulationCategory,
			default_value: float,
			start_trigger: float,
			end_trigger: float,
			is_active: bool = False
	):
		"""
			value constructor

			:param name: name of the simulation
			:param description: description of the simulation
			:param start_text:
			:param end_text:
			:param category: category of the simulation
			:param default_value: default value of the simulation
			:param start_trigger:
			:param end_trigger:
			:param is_active:
		"""
		self.name = name
		self.description = description
		self.start_text = start_text
		self.end_text = end_text
		self.category = category
		
		self.start_trigger = start_trigger
		self.end_trigger = end_trigger
		
		# values
		self.default_value = default_value
		self.value = default_value
		self.new_value = 0.0
		self.is_active = is_active
		
		self.effects = []
	
	def prepare(self):
		"""
			prepares the values for iteration

			:return: (nothing)
		"""
		self.new_value = 0.0
	
	def iterate(self, simulation):
		"""
			evaluates the values during iteration

			:param simulation: simulation that is updated
			:return: (nothing)
		"""
		self.value = self.default_value + self.new_value
		
		if self.is_active and self.value < self.end_trigger:
			self.is_active = False
			simulation.started_situations.append(self)
		elif not self.is_active and self.value > self.start_trigger:
			self.is_active = True
			simulation.ended_situations.append(self)
		
		# effects are sent, when the situation is active
		for effect in self.effects:
			if self.is_active:
				tmp_value = 1.0
			else:
				tmp_value = 0.0
			
			without_mood = effect.target_name.replace('_mood', '')
			without_freq = effect.target_name.replace('_freq', '')
			
			if effect.target_name in simulation.simulations:
				simulation.simulations[effect.target_name].new_value += effect.evaluate(tmp_value)
			elif without_mood in simulation.groups:
				simulation.groups[without_mood].mood.new_value += effect.evaluate(tmp_value)
			elif without_freq in simulation.groups:
				simulation.groups[without_freq].freq.new_value += effect.evaluate(tmp_value)
			else:
				raise Exception(f'cant get {effect.target_name} as simulation value')
	
	def finish(self):
		"""
			post processes values after iteration

			:return: (nothing)
		"""

	def print(self):
		"""
			print the current name and value

			:return: (nothing)
		"""
		print(f'{self.name:24}: \t{self.value:.2f} => {self.is_active}')
	
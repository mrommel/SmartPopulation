""" base types of simulations """

from enum import Enum


class SimulationEmotion(Enum):
	"""
		enum that represents the emotion towards a simulation simulation
	"""
	unknown = 0
	high_good = 1
	high_bad = 2


class BasicType(Enum):
	"""
		enum of the base types
	"""
	simulation = 0
	situation = 1
	policy = 2
	voter_group = 3


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
	tax = 6
	
	hidden = 10
	people = 20
	
	def __str__(self):
		return self.name
	
	@property
	def title(self):
		if self.value == SimulationCategory.public_services.value:
			return 'Public Services'
		elif self.value == SimulationCategory.law_and_order.value:
			return 'Law and order'
		elif self.value == SimulationCategory.economy.value:
			return 'Economy'
		elif self.value == SimulationCategory.foreign_policy.value:
			return 'Foreign policy'
		elif self.value == SimulationCategory.welfare.value:
			return 'Welfare'
		elif self.value == SimulationCategory.transport.value:
			return 'Transport'
		elif self.value == SimulationCategory.tax.value:
			return 'Taxes'
		elif self.value == SimulationCategory.people.value:
			return 'People'
		else:
			return 'default'
		
	def simulations(self, sim):
		return {
			k: simulation_item for k, simulation_item in sim.simulations.items() if
			simulation_item.category.value == self.value
		}
	
	def situations(self, sim):
		return {
			k: situation_item for k, situation_item in sim.situations.items() if
			situation_item.category.value == self.value
		}
	
	def policies(self, sim):
		return {
			k: policy_item for k, policy_item in sim.policies.items() if
			policy_item.category.value == self.value
		}


class Effect:
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


class ValueBase:
	"""
		base class of inputs / effects
	"""
	
	def __init__(self, key: str, name: str, icon: str, base_type: BasicType, value: float):
		"""
			value constructor
		
			:param key: key of the effect or input
			:param name: name of the effect or input
			:param icon: icon of the effect or input
			:param base_type: one of the basic type
			:param value: value of the effect or input
		"""
		self.key = key
		self.name = name
		self.icon = icon
		self.base_type = base_type
		self.value = value


class SimulationBase:
	"""
		base class of all simulations
	"""
	
	def __init__(
			self,
			name: str,
			description: str,
			category: SimulationCategory,
			icon: str = 'simulation_default.png',
			default_value: float = 0.5,
			min_value: float = 0.0,
			max_value: float = 1.0,
			emotion: SimulationEmotion = SimulationEmotion.unknown
	):
		"""
			value constructor
		
			:param name: name of the simulation
			:param description: description of the simulation
			:param category: category of the simulation
			:param icon: name of the icon
			:param default_value: default value of the simulation
			:param min_value: minimal value
			:param max_value: maximal value
		"""
		self.name = name
		self.description = description
		self.category = category
		self.icon = icon
		
		# values
		self.default_value = default_value
		self.value = default_value
		self.new_value = default_value
		self.min_value = min_value
		self.max_value = max_value
		self.emotion = emotion
		
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
		
			:returns: (nothing)
		"""
		print(f'{self.name:24}: \t{self.value:.2f}')
	
	def cause_values(self, sim) -> [ValueBase]:
		"""
			get the simulations, situations or policies that have impact on this simulation
		
			:param sim: the Simulation to find the connections in
			:type sim: Simulation
			:returns: list of (ValueBase)
			:rtype: [ValueBase]
		"""
		
		cause_list = []
		
		own_key = next((key for key, sim_item in sim.simulations.items() if sim_item.name == self.name), None)
		
		if own_key is None:
			own_key = next((key for key, group_item in sim.groups.items() if group_item.mood.name == self.name), None)
			if own_key is not None:
				own_key = f'{own_key}_mood'
			
		if own_key is None:
			own_key = next((key for key, group_item in sim.groups.items() if group_item.freq.name == self.name), None)
			if own_key is not None:
				own_key = f'{own_key}_freq'
		
		for key, simulation_item in sim.simulations.items():
			for effect in simulation_item.effects:
				if effect.target_name == own_key:
					cause_list.append(
						ValueBase(
							key,
							simulation_item.name,
							simulation_item.icon,
							BasicType.simulation,
							effect.evaluate(self.value)
						)
					)
		
		for key, situation_item in sim.situations.items():
			for effect in situation_item.effects:
				if effect.target_name == own_key:
					cause_list.append(
						ValueBase(
							key,
							situation_item.name,
							'icon',
							BasicType.situation,
							effect.evaluate(self.value)
						)
					)
		
		for key, policy_item in sim.policies.items():
			for effect in policy_item.effects:
				if effect.target_name == own_key:
					cause_list.append(
						ValueBase(
							key,
							policy_item.name,
							'icon',
							BasicType.policy,
							effect.evaluate(self.value)
						)
					)
		
		# print(f'cause_values of {own_key} of {self.name} => {len(cause_list)}')
		
		return cause_list
	
	def effect_values(self, simulation) -> [ValueBase]:
		
		effect_list = []
		
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
				simulation_name = simulation.simulations[effect.target_name].name
				simulation_icon = simulation.simulations[effect.target_name].icon
				effect_list.append(
					ValueBase(effect.target_name, simulation_name, simulation_icon, BasicType.simulation, effect.evaluate(tmp_value)))
			elif effect.target_name in simulation.situations:
				situation_name = simulation.situations[effect.target_name].name
				effect_list.append(
					ValueBase(effect.target_name, situation_name, 'icon', BasicType.situation, effect.evaluate(tmp_value)))
			elif without_mood in simulation.groups:
				voter_name = f'{simulation.groups[without_mood].name} (Mood)'
				effect_list.append(
					ValueBase(without_mood, voter_name, 'icon', BasicType.voter_group, effect.evaluate(tmp_value)))
			elif without_freq in simulation.groups:
				voter_name = f'{simulation.groups[without_freq].name} (Frequency)'
				effect_list.append(
					ValueBase(without_freq, voter_name, 'icon', BasicType.voter_group, effect.evaluate(tmp_value)))
		
		return effect_list


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
		
		# debug
		# print(f'Group "{self.name}" with')
		# print(f'  * mood: {self.mood.value} => {self.mood.history}')
		# print(f'  * freq: {self.freq.value} => {self.freq.history}')
	
	def print(self):
		"""
			print the current name and value

			:return: (nothing)
		"""
		print(self)

	def __repr__(self):
		"""
			string representation of `GroupBase`
		"""
		return f'<Group {self.name:24}: \tfreq={self.freq.value * 100.0:.2f}% / \tmood={self.mood.value}>'


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
		self.value = self.default_value + self.new_value
		
		if self.is_active and self.value < self.end_trigger:
			self.is_active = False
			simulation.ended_situations.append(self)
		elif not self.is_active and self.value > self.start_trigger:
			self.is_active = True
			simulation.started_situations.append(self)
		
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
			elif effect.target_name in simulation.situations:
				simulation.situations[effect.target_name].new_value += effect.evaluate(tmp_value)
			elif without_mood in simulation.groups:
				simulation.groups[without_mood].mood.new_value += effect.evaluate(tmp_value)
			elif without_freq in simulation.groups:
				simulation.groups[without_freq].freq.new_value += effect.evaluate(tmp_value)
			else:
				raise Exception(f'cant get "{effect.target_name}" as simulation value')
	
	def finish(self):
		"""
			post processes values after iteration

			:return: (nothing)
		"""
		# put to history
		self.history.insert(0, self.value)
	
	def print(self):
		"""
			print the current name and value

			:return: (nothing)
		"""
		print(f'{self.name:24}: \t{self.value:.2f} => {self.is_active}')
	
	def cause_values(self, simulation) -> [ValueBase]:
		"""
			get the list of causes (input values) for this situation (they have effects towards this)

			:param simulation: simulation where the causes are in
			:returns: array of causes (input values) for this situation
		"""
		
		cause_list = []
		
		own_key = next((key for key, sit_item in simulation.situations.items() if sit_item.name == self.name), None)
		
		for key, simulation_item in simulation.simulations.items():
			for effect in simulation_item.effects:
				if effect.target_name == own_key:
					cause_list.append(ValueBase(key, simulation_item.name, simulation_item.icon, BasicType.simulation, 0.0))
		
		for key, policy_item in simulation.policies.items():
			for effect in policy_item.effects:
				if effect.target_name == own_key:
					cause_list.append(ValueBase(key, policy_item.name, 'icon', BasicType.policy, 0.0))

		# note: a situation does not cause changes to another situation so far
		
		return cause_list
	
	def effect_values(self, simulation) -> [ValueBase]:
		"""
			get the list of effects of this situation

			:param simulation: simulation where the effects are in
			:returns: array of effects (output values) for this situation
		"""
		
		effect_list = []
		
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
				simulation_name = simulation.simulations[effect.target_name].name
				simulation_icon = simulation.simulations[effect.target_name].icon
				effect_list.append(
					ValueBase(effect.target_name, simulation_name, simulation_icon, BasicType.simulation, effect.evaluate(tmp_value)))
			elif effect.target_name in simulation.situations:
				situation_name = simulation.situations[effect.target_name].name
				effect_list.append(
					ValueBase(effect.target_name, situation_name, 'icon', BasicType.situation, effect.evaluate(tmp_value)))
			elif without_mood in simulation.groups:
				voter_name = f'{simulation.groups[without_mood].name} (Mood)'
				effect_list.append(
					ValueBase(without_mood, voter_name, 'icon', BasicType.voter_group, effect.evaluate(tmp_value)))
			elif without_freq in simulation.groups:
				voter_name = f'{simulation.groups[without_freq].name} (Frequency)'
				effect_list.append(
					ValueBase(without_freq, voter_name, 'icon', BasicType.voter_group, effect.evaluate(tmp_value)))
		
		return effect_list


class PolicyBase:
	"""
		base class for policies
	"""
	
	def __init__(
			self,
			name: str,
			description: str,
			category: SimulationCategory,
			slider: [str],
			can_be_cancelled: bool,
			introduce: int,
			cancel: int,
			raise_cost: int,
			lower_cost: int,
			min_cost: int,
			max_cost: int,
			implementation: int,
			min_income: int,
			max_income: int
	):
		"""
			value constructor

			:param name: name of the policy
			:param description: description of the policy
			:param category: category of the policy
		"""
		self.name = name
		self.description = description
		self.category = category
		self.slider = slider
		self.can_be_cancelled = can_be_cancelled
		self.introduce = introduce
		self.cancel = cancel
		self.raise_cost = raise_cost
		self.lower_cost = lower_cost
		self.min_cost = min_cost
		self.max_cost = max_cost
		self.implementation = implementation
		self.min_income = min_income
		self.max_income = max_income
		
		self.is_active = not can_be_cancelled  # if it cant be cancelled, it must be active
		self.slider_value = 'NONE'
		self.value = 0.0

		self.cost_multiplier = []
		self.income_multiplier = []
		self.effects = []
		self.history = []
		
	def prepare(self):
		"""
			prepares the values for iteration

			:return: (nothing)
		"""
	
	def iterate(self, simulation):
		"""
			evaluates the values during iteration

			:param simulation: simulation that is updated
			:return: (nothing)
		"""
		if not self.is_active:
			return
		
		# effects are sent, when the situation is active
		for effect in self.effects:
			
			without_mood = effect.target_name.replace('_mood', '')
			without_freq = effect.target_name.replace('_freq', '')
			
			if effect.target_name in simulation.simulations:
				simulation.simulations[effect.target_name].new_value += effect.evaluate(self.value)
			elif effect.target_name in simulation.situations:
				simulation.situations[effect.target_name].new_value += effect.evaluate(self.value)
			elif without_mood in simulation.groups:
				simulation.groups[without_mood].mood.new_value += effect.evaluate(self.value)
			elif without_freq in simulation.groups:
				simulation.groups[without_freq].freq.new_value += effect.evaluate(self.value)
			else:
				raise Exception(f'cant get {effect.target_name} as simulation value')
	
	def finish(self):
		"""
			post processes values after iteration

			:return: (nothing)
		"""
		# put to history
		self.history.insert(0, self.value)
	
	def print(self):
		"""
			print the current name and value

			:return: (nothing)
		"""
		print(f'{self.name:24}: \t{self.value:.2f}')
	
	def effect_values(self, simulation) -> [ValueBase]:
		
		effect_list = []
		
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
				simulation_name = simulation.simulations[effect.target_name].name
				simulation_icon = simulation.simulations[effect.target_name].icon
				effect_list.append(
					ValueBase(effect.target_name, simulation_name, simulation_icon, BasicType.simulation, effect.evaluate(tmp_value)))
			elif effect.target_name in simulation.situations:
				situation_name = simulation.situations[effect.target_name].name
				effect_list.append(
					ValueBase(effect.target_name, situation_name, 'icon', BasicType.situation, effect.evaluate(tmp_value)))
			elif without_mood in simulation.groups:
				voter_name = f'{simulation.groups[without_mood].name} (Mood)'
				effect_list.append(
					ValueBase(without_mood, voter_name, 'icon', BasicType.voter_group, effect.evaluate(tmp_value)))
			elif without_freq in simulation.groups:
				voter_name = f'{simulation.groups[without_freq].name} (Frequency)'
				effect_list.append(
					ValueBase(without_freq, voter_name, 'icon', BasicType.voter_group, effect.evaluate(tmp_value)))
		
		return effect_list
	
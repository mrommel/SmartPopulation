""" population simulation main module. """
import math

import plotly.graph_objects as go

from population import constants
from population.configuration import PopulationConfiguration
from population.data import SimulationData


class Population:
	"""
		main population class
	"""
	def __init__(self, config: PopulationConfiguration, data: SimulationData):
		"""
			value constructor
			
			:param config: configuration of the population simulation
			:param data: initial data of the population simulation
		"""
		self.current_fertility_param: int = 0
		self.config = config
		self.data = data
		
	def calculate_babies(self, fertility, number_of_females):
		"""
			calculate the amount of babies born based on the current distribution
		
			:param fertility: current fertility
			:param number_of_females: number of females in one generation
			:return: number of babies
		"""
		
		_tmp_pow = 100.0 / self.current_fertility_param
		_tmp_ki = pow(fertility, _tmp_pow)
		_tmp_b = self.current_fertility_param / 100.0
		_tmp_val = number_of_females * (_tmp_ki * _tmp_b / 1.28)
		
		if _tmp_val < 0.0:
			return 0.0
		
		return _tmp_val
		
	# k param
	def fertility(self, age):
		"""
			get fertility of generation / age group
			
			:param age: generation / age group
			:return: fertility
		"""
		# print('fertility for %d = %f' % (age, constants.param_k[age]))
		return constants.param_k[age]
	
	def param_a0(self, age):
		"""
			a0 paramater of generation / age group
			
			:param age: generation / age group
			:return: a0 param
		"""
		return constants.param_a0[age]
	
	def param_a1(self, age):
		"""
			a1 paramater of generation / age group

			:param age: generation / age group
			:return: a1 param
		"""
		return constants.param_a1[age]
	
	def update_males(self, age):
		"""
			moves one generation of males to next

			:param age: age of this generation
			:return: new amount of males in next generation (one year older)
		"""
		
		# recovery of the value i - 1 to be changed
		_tmp_val = self.data.number_of_males(age - 1)
		
		# recovery of value 84
		_tmp_val84 = self.data.number_of_males(84)
		
		# retrieve param a0 for age i
		_tmp_a0 = self.param_a0(age)
		# retrieve param a0 for age 84
		_tmp_a084 = self.param_a0(84)
		
		# retrieve param a1 for age i
		_tmp_a1 = self.param_a1(age)
		# retrieve param a1 for age 84
		_tmp_a184 = self.param_a1(84)
		
		if age == 1:
			_tmp_res = _tmp_a0 + _tmp_a1 * math.log10(100 - self.config.life_expectancy)
			_new_val = _tmp_val - _tmp_val * (pow(10, _tmp_res) / 1000)
		elif 2 <= age < 5:
			_tmp_res = 1 - math.exp(
				0.25 * math.log(
					1 - math.pow(10, _tmp_a0 + _tmp_a1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_new_val = _tmp_val - _tmp_val * _tmp_res
		elif 5 <= age <= 84:
			_tmp_res = 1 - math.exp(
				0.20 * math.log(
					1 - math.pow(10, _tmp_a0 + _tmp_a1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_new_val = _tmp_val - _tmp_val * _tmp_res
		elif 85 <= age <= 89:
			_tmp_res = 1 - math.exp(
				0.20 * math.log(
					1 - math.pow(10, _tmp_a084 + _tmp_a184 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_new_val = _tmp_val - _tmp_val * ((0.3378 + 0.69798 * 5 * _tmp_res) / 5)
		elif 90 <= age <= 94:
			_new_val = _tmp_val - _tmp_val * 0.25
		elif 95 <= age <= 99:
			_new_val = _tmp_val - _tmp_val * 0.4
		elif 100 <= age <= 109:
			_new_val = _tmp_val - _tmp_val * 0.5
		else:
			_new_val = _tmp_val - _tmp_val  # dumb because 0
		
		return _new_val
	
	def update_females(self, age):
		"""
			moves one generation of females to next
		
			:param age: age of this generation
			:return: new amount of females in next generation (one year older)
		"""
		
		# recovery of the value i - 1 to be changed
		_tmp_val = self.data.number_of_females(age - 1)
		
		# recovery of value 84
		_tmp_val84 = self.data.number_of_females(84)
		
		# retrieve param a0 for age i
		_tmp_a0 = self.param_a0(age)
		# retrieve param a0 for age 84
		_tmp_a084 = self.param_a0(84)
		
		# retrieve param a1 for age i
		_tmp_a1 = self.param_a1(age)
		# retrieve param a1 for age 84
		_tmp_a184 = self.param_a1(84)
		
		if age == 1:
			_tmp_res = _tmp_a0 + _tmp_a1 * math.log10(100 - self.config.life_expectancy)
			_new_val = _tmp_val - _tmp_val * (math.pow(10, _tmp_res) / 1000)
		elif 2 <= age < 5:
			_tmp_res = 1 - math.exp(
				0.25 * math.log(
					1 - math.pow(10, _tmp_a0 + _tmp_a1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_new_val = _tmp_val - _tmp_val * _tmp_res
		elif 5 <= age <= 84:
			_tmp_res = 1 - math.exp(
				0.20 * math.log(
					1 - math.pow(10, _tmp_a0 + _tmp_a1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_new_val = _tmp_val - _tmp_val * _tmp_res
		elif 85 <= age <= 89:
			_tmp_res = 1 - math.exp(
				0.20 * math.log(
					1 - math.pow(10, _tmp_a084 + _tmp_a184 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_new_val = _tmp_val - _tmp_val * ((0.3378 + 0.69798 * 5 * _tmp_res) / 5)
		elif 90 <= age <= 94:
			_new_val = _tmp_val - _tmp_val * 0.15
		elif 95 <= age <= 99:
			_new_val = _tmp_val - _tmp_val * 0.2
		elif 100 <= age <= 109:
			_new_val = _tmp_val - _tmp_val * 0.3
		else:
			_new_val = _tmp_val - _tmp_val  # just as stupid because 0
		
		return _new_val
	
	@property
	def population(self):
		"""
			sums up total population of this simulation
			
			:return: total population of this simulation
		"""
		total_population = 0
		for age in range(0, 100):
			females = self.data.number_of_females(age)
			males = self.data.number_of_males(age)
			total_population += females + males
		
		return total_population
	
	def print_curve(self, year):
		"""
			logs current simulation data to console
		
			:param year: year (just for display)
			:return: (nothing, prints statements to console)
		"""
		
		print('-----------------------------')
		print('population curve for ', year)
		print('-----------------------------')
		total_population = 0
		for age in range(0, 100):
			females = self.data.number_of_females(age)
			males = self.data.number_of_males(age)
			total_population += females + males
			print('age=', age, ' =>', males, '|', females)
		
		print('-----------------------------')
		print('total population ', total_population)
		print('-----------------------------')
	
	def show_chart(self, year):
		"""
			show a chart of the current simulation data
		
			:param year: year (just for display)
			:return: (nothing, opens browser with chart)
		"""
		y_age = list(range(0, 100))
		x_male = [self.data.number_of_males(age) for age in range(0, 100)]
		x_female = [-self.data.number_of_females(age) for age in range(0, 100)]
		
		# Creating instance of the figure
		fig = go.Figure()
		
		# Adding Male data to the figure
		fig.add_trace(go.Bar(y=y_age, x=x_male, name='Male', orientation='h'))
		
		# Adding Female data to the figure
		fig.add_trace(go.Bar(y=y_age, x=x_female, name='Female', orientation='h'))
		
		# Updating the layout for our graph
		fig.update_layout(
			title=f'Population Pyramid of Germany {year}',
			title_font_size=22,
			yaxis=go.layout.YAxis(title='Age'),
			xaxis=go.layout.XAxis(
				range=[min(x_female), max(x_male)],
				# tickvals=xtick,
				# ticktext=[str(abs(x)) for x in xtick],
				title='Number'),
			barmode='overlay',
			bargap=0.1,
			bargroupgap=0
		)
		
		fig.show()
	
	# updatePerformanceParam
	def update_fertility(self):
		"""
			update the internal current fertility value from number_of_children_per_women
			
			:return: (nothing)
		"""
		
		_old_item = {}
		_down_param = {}
		_up_param = {}
		
		for key, mapping_value in constants.mapping_fertility.items():
			if self.config.number_of_children_per_women <= mapping_value:
				_down_param = _old_item
				_up_param['title'] = key
				_up_param['data'] = mapping_value
				break
			
			_old_item['title'] = key
			_old_item['data'] = mapping_value
		
		_val_up = _up_param['data']
		_val_down = _down_param['data']
		_param_up = _up_param['title']
		_param_down = _down_param['title']
		
		_new_param = _param_down + ((_param_up - _param_down) / (_val_up - _val_down)) * (
				self.config.number_of_children_per_women - _val_down)
		
		self.current_fertility_param = _new_param
	
	def iterate(self):
		"""
			runs one iteration (aka one year) of this simulation
		
			:return: (nothing)
		"""
		
		self.update_fertility()
		
		total_babies = 0
		old_total_population = 0
		total_population = 0
		
		# max_men = 0  # reset the number of men
		# max_women = 0  # female count reset
		
		for age in reversed(range(1, 100)):
			# calculate the number of babies
			number_of_females_in_age = self.data.number_of_females(age)
			fertility_in_age = self.fertility(age + 1)
			total_babies_of_age = self.calculate_babies(fertility_in_age, number_of_females_in_age)
			# print("number_of_females: ", number_of_females_in_age)
			# print("babies per age: ", total_babies_of_age)
			
			total_babies += total_babies_of_age
			
			old_total_males_data = self.data.number_of_males(age)
			old_total_females_data = self.data.number_of_females(age)
			
			# addition of past total population
			old_total_population += old_total_males_data + old_total_females_data
			
			# recovery of the number of men
			year_males_data = self.update_males(age)
			# retrieval of the number of women
			year_females_data = self.update_females(age)
			
			# recovery of the maximum number of man
			# if year_males_data >= max_men:
			# 	max_men = year_males_data
			# recovery of the maximum number of women
			# if year_females_data >= max_women:
			# 	max_women = year_females_data
			
			# addition of the current total population
			total_population = total_population + year_males_data + year_females_data
			
			# Add the values to the new array.
			self.data.set_number_of_males(age, year_males_data)
			self.data.set_number_of_females(age, year_females_data)
		
		# addition of the past total population of old newborns
		old_total_population += self.data.number_of_males(0)
		old_total_population += self.data.number_of_females(0)
		
		# print('--- debug ---')
		# print(' total babies: ', int(total_babies))
		# print(' total_population: ', int(total_population))
		# print(' old_total_population: ', old_total_population)
		
		male_babies = total_babies * (self.config.boys_ratio / 100.0)
		female_babies = total_babies * (1.0 - (self.config.boys_ratio / 100.0))
		
		# if male_babies >= max_men:
		# 	max_men = male_babies
		# if female_babies >= max_women:
		# 	max_women = female_babies
		
		self.data.set_number_of_males(0, male_babies)
		self.data.set_number_of_females(0, female_babies)

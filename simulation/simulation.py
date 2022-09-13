import math

from simulation.configuration import SimulationConfiguration
import plotly.graph_objects as go

from simulation import constants
from simulation.data import SimulationData


class Simulation:
	def __init__(self, config: SimulationConfiguration, data: SimulationData):
		self.currentFertilityParam: int = 0
		self.config = config
		self.data = data
	
	# getSimulationLibreBabies (_n,_val)
	def calculate_babies(self, fertility, number_of_females):
		
		_tmpPow = 100.0 / self.currentFertilityParam
		_tmpKi = pow(fertility, _tmpPow)
		_tmpB = self.currentFertilityParam / 100.0
		_tmpVal = number_of_females * (_tmpKi * _tmpB / 1.28)
		
		if _tmpVal < 0.0:
			return 0.0
		
		return _tmpVal
	
	# k param
	def fertility(self, age):
		# print('fertility for %d = %f' % (age, constants.param_k[age]))
		return constants.param_k[age]
	
	def param_a0(self, age):
		return constants.param_a0[age]
	
	def param_a1(self, age):
		return constants.param_a1[age]
	
	# calculate the number of males
	def update_males(self, age):
		
		# recovery of the value i - 1 to be changed
		_tmpVal = self.data.number_of_males(age - 1)
		
		# recovery of value 84
		_tmpVal84 = self.data.number_of_males(84)
		
		# retrieve param a0 for age i
		_tmpA0 = self.param_a0(age)
		# retrieve param a0 for age 84
		_tmpA084 = self.param_a0(84)
		
		# retrieve param a1 for age i
		_tmpA1 = self.param_a1(age)
		# retrieve param a1 for age 84
		_tmpA184 = self.param_a1(84)
		
		if age == 1:
			_tmpRes = _tmpA0 + _tmpA1 * math.log10(100 - self.config.life_expectancy)
			_newVal = _tmpVal - _tmpVal * (pow(10, _tmpRes) / 1000)
		elif 2 <= age < 5:
			_tmpRes = 1 - math.exp(
				0.25 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 5 <= age <= 84:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 85 <= age <= 89:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA084 + _tmpA184 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * ((0.3378 + 0.69798 * 5 * _tmpRes) / 5)
		elif 90 <= age <= 94:
			_newVal = _tmpVal - _tmpVal * 0.25
		elif 95 <= age <= 99:
			_newVal = _tmpVal - _tmpVal * 0.4
		elif 100 <= age <= 109:
			_newVal = _tmpVal - _tmpVal * 0.5
		else:
			_newVal = _tmpVal - _tmpVal  # dumb because 0
		
		return _newVal
	
	# calculation of the number of women function
	def update_females(self, age):
		
		# recovery of the value i - 1 to be changed
		_tmpVal = self.data.number_of_females(age - 1)
		
		# recovery of value 84
		_tmpVal84 = self.data.number_of_females(84)
		
		# retrieve param a0 for age i
		_tmpA0 = self.param_a0(age)
		# retrieve param a0 for age 84
		_tmpA084 = self.param_a0(84)
		
		# retrieve param a1 for age i
		_tmpA1 = self.param_a1(age)
		# retrieve param a1 for age 84
		_tmpA184 = self.param_a1(84)
		
		if age == 1:
			_tmpRes = _tmpA0 + _tmpA1 * math.log10(100 - self.config.life_expectancy)
			_newVal = _tmpVal - _tmpVal * (math.pow(10, _tmpRes) / 1000)
		elif 2 <= age < 5:
			_tmpRes = 1 - math.exp(
				0.25 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 5 <= age <= 84:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 85 <= age <= 89:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA084 + _tmpA184 * math.log10(100 - self.config.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * ((0.3378 + 0.69798 * 5 * _tmpRes) / 5)
		elif 90 <= age <= 94:
			_newVal = _tmpVal - _tmpVal * 0.15
		elif 95 <= age <= 99:
			_newVal = _tmpVal - _tmpVal * 0.2
		elif 100 <= age <= 109:
			_newVal = _tmpVal - _tmpVal * 0.3
		else:
			_newVal = _tmpVal - _tmpVal  # just as stupid because 0
		
		return _newVal
	
	@property
	def population(self):
		total_population = 0
		for age in range(0, 100):
			females = self.data.number_of_females(age)
			males = self.data.number_of_males(age)
			total_population += females + males
		
		return total_population
	
	def print_curve(self, year):
		
		print('-----------------------------')
		print('population curve for ', year)
		print('-----------------------------')
		total_population = 0
		for age in range(0, 100):
			females = self.number_of_females(age)
			males = self.number_of_males(age)
			total_population += females + males
			print('age=', age, ' =>', males, '|', females)
		
		print('-----------------------------')
		print('total population ', total_population)
		print('-----------------------------')
	
	def show_chart(self, year):
		y_age = [age for age in range(0, 100)]
		x_male = [self.number_of_males(age) for age in range(0, 100)]
		x_female = [-self.number_of_females(age) for age in range(0, 100)]
		
		# Creating instance of the figure
		fig = go.Figure()
		
		# Adding Male data to the figure
		fig.add_trace(go.Bar(y=y_age, x=x_male, name='Male', orientation='h'))
		
		# Adding Female data to the figure
		fig.add_trace(go.Bar(y=y_age, x=x_female, name='Female', orientation='h'))
		
		# Updating the layout for our graph
		fig.update_layout(
			title='Population Pyramid of Germany %d' % year,
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
		
		_oldItem = {}
		_downParam = {}
		_upParam = {}
		
		for key in constants.mapping_fertility:
			mapping_value = constants.mapping_fertility[key]
			if self.config.number_of_children_per_women <= mapping_value:
				_downParam = _oldItem
				_upParam['title'] = key
				_upParam['data'] = mapping_value
				break
			
			_oldItem['title'] = key
			_oldItem['data'] = mapping_value
		
		_valUp = _upParam['data']
		_valDown = _downParam['data']
		_paramUp = _upParam['title']
		_paramDown = _downParam['title']
		
		_newParam = _paramDown + ((_paramUp - _paramDown) / (_valUp - _valDown)) * (
				self.config.number_of_children_per_women - _valDown)
		
		self.currentFertilityParam = _newParam
	
	def iterate(self):
		
		self.update_fertility()
		
		total_babies = 0
		old_total_population = 0
		total_population = 0
		
		_maxH = 0  # reset the number of men
		_maxF = 0  # female count reset
		
		for age in reversed(range(1, 100)):
			# calculate the number of babies
			number_of_females_in_age = self.data.number_of_females(age)
			fertility_in_age = self.fertility(age + 1)
			total_babies_of_age = self.calculate_babies(fertility_in_age, number_of_females_in_age)
			# print("number_of_females: ", number_of_females_in_age)
			# print("babies per age: ", total_babies_of_age)
			
			total_babies += total_babies_of_age
			
			_oldTotalHData = self.data.number_of_males(age)
			_oldTotalFData = self.data.number_of_females(age)
			
			# addition of past total population
			old_total_population += _oldTotalHData + _oldTotalFData
			
			# recovery of the number of men
			_yearHData = self.update_males(age)
			# retrieval of the number of women
			_yearFData = self.update_females(age)
			
			# recovery of the maximum number of man
			if _yearHData >= _maxH:
				_maxH = _yearHData
			# recovery of the maximum number of women
			if _yearFData >= _maxF:
				_maxF = _yearFData
			
			# addition of the current total population
			total_population = total_population + _yearHData + _yearFData
			
			# Add the values to the new array.
			self.data.set_number_of_males(age, _yearHData)
			self.data.set_number_of_females(age, _yearFData)
		
		# addition of the past total population of old newborns
		old_total_population += self.data.number_of_males(0)
		old_total_population += self.data.number_of_females(0)
		
		# print('--- debug ---')
		# print(' total babies: ', int(total_babies))
		# print(' total_population: ', int(total_population))
		# print(' old_total_population: ', old_total_population)
		
		male_babies = total_babies * (self.config.boys_ratio / 100.0)
		female_babies = total_babies * (1.0 - (self.config.boys_ratio / 100.0))
		
		if male_babies >= _maxH:
			_maxH = male_babies
		if female_babies >= _maxF:
			_maxF = female_babies
		
		self.data.set_number_of_males(0, male_babies)
		self.data.set_number_of_females(0, female_babies)
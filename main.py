import constants
import math
import plotly.graph_objects as go


class SimulationRecord:
	def __init__(self, age, men, women):
		self.age = age
		self.men = men
		self.women = women


class Simulation:
	def __init__(self):
		self.currentFertilityParam = 17.22
		self.life_expectancy = 81.8  # in years
		self.number_of_children_per_women = 1.62
		self.boys_ratio = 51.4
		
		self.data = []
		
		# https://service.destatis.de/bevoelkerungspyramide/#! from 2019 for germany
		self.data.append(SimulationRecord(99, 2000, 11000))
		self.data.append(SimulationRecord(98, 3000, 16000))
		self.data.append(SimulationRecord(97, 5000, 22000))
		self.data.append(SimulationRecord(96, 7000, 30000))
		self.data.append(SimulationRecord(95, 11000, 42000))
		self.data.append(SimulationRecord(94, 18000, 58000))
		self.data.append(SimulationRecord(93, 25000, 73000))
		self.data.append(SimulationRecord(92, 35000, 89000))
		self.data.append(SimulationRecord(91, 50000, 113000))
		self.data.append(SimulationRecord(90, 63000, 134000))
		
		self.data.append(SimulationRecord(89, 79000, 159000))
		self.data.append(SimulationRecord(88, 90000, 170000))
		self.data.append(SimulationRecord(87, 104000, 185000))
		self.data.append(SimulationRecord(86, 122000, 203000))
		self.data.append(SimulationRecord(85, 172000, 273000))
		self.data.append(SimulationRecord(84, 207000, 316000))
		self.data.append(SimulationRecord(83, 237000, 346000))
		self.data.append(SimulationRecord(82, 266000, 375000))
		self.data.append(SimulationRecord(81, 306000, 417000))
		self.data.append(SimulationRecord(80, 348000, 464000))
		
		self.data.append(SimulationRecord(79, 372000, 482000))
		self.data.append(SimulationRecord(78, 370000, 466000))
		self.data.append(SimulationRecord(77, 317000, 387000))
		self.data.append(SimulationRecord(76, 337000, 405000))
		self.data.append(SimulationRecord(75, 339000, 404000))
		self.data.append(SimulationRecord(74, 257000, 306000))
		self.data.append(SimulationRecord(73, 302000, 348000))
		self.data.append(SimulationRecord(72, 354000, 402000))
		self.data.append(SimulationRecord(71, 384000, 429000))
		self.data.append(SimulationRecord(70, 425000, 474000))
		
		self.data.append(SimulationRecord(69, 444000, 495000))
		self.data.append(SimulationRecord(68, 449000, 498000))
		self.data.append(SimulationRecord(67, 463000, 511000))
		self.data.append(SimulationRecord(66, 469000, 514000))
		self.data.append(SimulationRecord(65, 492000, 531000))
		self.data.append(SimulationRecord(64, 510000, 539000))
		self.data.append(SimulationRecord(63, 534000, 555000))
		self.data.append(SimulationRecord(62, 555000, 571000))
		self.data.append(SimulationRecord(61, 573000, 585000))
		self.data.append(SimulationRecord(60, 611000, 621000))
		
		self.data.append(SimulationRecord(59, 632000, 640000))
		self.data.append(SimulationRecord(58, 658000, 663000))
		self.data.append(SimulationRecord(57, 673000, 672000))
		self.data.append(SimulationRecord(56, 701000, 694000))
		self.data.append(SimulationRecord(55, 710000, 700000))
		self.data.append(SimulationRecord(54, 701000, 688000))
		self.data.append(SimulationRecord(53, 699000, 688000))
		self.data.append(SimulationRecord(52, 683000, 672000))
		self.data.append(SimulationRecord(51, 667000, 655000))
		self.data.append(SimulationRecord(50, 639000, 626000))
		
		self.data.append(SimulationRecord(49, 595000, 586000))
		self.data.append(SimulationRecord(48, 574000, 566000))
		self.data.append(SimulationRecord(47, 523000, 516000))
		self.data.append(SimulationRecord(46, 483000, 479000))
		self.data.append(SimulationRecord(45, 480000, 476000))
		self.data.append(SimulationRecord(44, 476000, 468000))
		self.data.append(SimulationRecord(43, 488000, 482000))
		self.data.append(SimulationRecord(42, 500000, 490000))
		self.data.append(SimulationRecord(41, 504000, 495000))
		self.data.append(SimulationRecord(40, 512000, 502000))
		
		self.data.append(SimulationRecord(39, 539000, 527000))
		self.data.append(SimulationRecord(38, 538000, 525000))
		self.data.append(SimulationRecord(37, 546000, 526000))
		self.data.append(SimulationRecord(36, 537000, 515000))
		self.data.append(SimulationRecord(35, 538000, 513000))
		self.data.append(SimulationRecord(34, 543000, 515000))
		self.data.append(SimulationRecord(33, 561000, 530000))
		self.data.append(SimulationRecord(32, 575000, 537000))
		self.data.append(SimulationRecord(31, 590000, 547000))
		self.data.append(SimulationRecord(30, 576000, 537000))
		
		self.data.append(SimulationRecord(29, 586000, 542000))
		self.data.append(SimulationRecord(28, 537000, 497000))
		self.data.append(SimulationRecord(27, 519000, 480000))
		self.data.append(SimulationRecord(26, 512000, 471000))
		self.data.append(SimulationRecord(25, 497000, 455000))
		self.data.append(SimulationRecord(24, 489000, 447000))
		self.data.append(SimulationRecord(23, 496000, 454000))
		self.data.append(SimulationRecord(22, 499000, 455000))
		self.data.append(SimulationRecord(21, 473000, 433000))
		self.data.append(SimulationRecord(20, 457000, 414000))
		
		self.data.append(SimulationRecord(19, 439000, 407000))
		self.data.append(SimulationRecord(18, 412000, 384000))
		self.data.append(SimulationRecord(17, 397000, 373000))
		self.data.append(SimulationRecord(16, 388000, 366000))
		self.data.append(SimulationRecord(15, 387000, 366000))
		self.data.append(SimulationRecord(14, 378000, 358000))
		self.data.append(SimulationRecord(13, 374000, 353000))
		self.data.append(SimulationRecord(12, 381000, 361000))
		self.data.append(SimulationRecord(11, 383000, 364000))
		self.data.append(SimulationRecord(10, 373000, 354000))
		
		self.data.append(SimulationRecord(9, 379000, 360000))
		self.data.append(SimulationRecord(8, 370000, 351000))
		self.data.append(SimulationRecord(7, 379000, 359000))
		self.data.append(SimulationRecord(6, 380000, 360000))
		self.data.append(SimulationRecord(5, 394000, 374000))
		self.data.append(SimulationRecord(4, 399000, 380000))
		self.data.append(SimulationRecord(3, 412000, 394000))
		self.data.append(SimulationRecord(2, 407000, 389000))
		self.data.append(SimulationRecord(1, 407000, 388000))
		self.data.append(SimulationRecord(0, 406000, 386000))
	
	# getSimulationLibreBabies (_n,_val)
	def calculate_babies(self, fertility, number_of_females):

		_tmpPow = 100.0 / self.currentFertilityParam
		_tmpKi = pow(fertility, _tmpPow)
		_tmpB = self.currentFertilityParam / 100.0
		_tmpVal = number_of_females * (_tmpKi * _tmpB / 1.28)
		
		if _tmpVal < 0.0:
			return 0.0
		
		return _tmpVal
	
	def number_of_females(self, age):
		return next(filter(lambda val: val.age == age, self.data), SimulationRecord(0, 0, 0)).women
	
	def number_of_males(self, age):
		return next(filter(lambda val: val.age == age, self.data), SimulationRecord(0, 0, 0)).men
	
	def set_number_of_females(self, age, value):
		item = next(filter(lambda val: val.age == age, self.data), SimulationRecord(0, -1, -1))
		
		if item.women == -1:
			self.data.append(SimulationRecord(age, 0, value))
		else:
			item.women = int(value)
	
	def set_number_of_males(self, age, value):
		item = next(filter(lambda val: val.age == age, self.data), SimulationRecord(0, -1, -1))
		
		if item.men == -1:
			self.data.append(SimulationRecord(age, value, 0))
		else:
			item.men = int(value)
	
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
		_tmpVal = self.number_of_males(age - 1)
		
		# recovery of value 84
		_tmpVal84 = self.number_of_males(84)
		
		# retrieve param a0 for age i
		_tmpA0 = self.param_a0(age)
		# retrieve param a0 for age 84
		_tmpA084 = self.param_a0(84)
		
		# retrieve param a1 for age i
		_tmpA1 = self.param_a1(age)
		# retrieve param a1 for age 84
		_tmpA184 = self.param_a1(84)
		
		if age == 1:
			_tmpRes = _tmpA0 + _tmpA1 * math.log10(100 - self.life_expectancy)
			_newVal = _tmpVal - _tmpVal * (pow(10, _tmpRes) / 1000)
		elif 2 <= age < 5:
			_tmpRes = 1 - math.exp(
				0.25 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.life_expectancy)) / 1000));
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 5 <= age <= 84:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.life_expectancy)) / 1000));
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 85 <= age <= 89:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA084 + _tmpA184 * math.log10(100 - self.life_expectancy)) / 1000));
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
		_tmpVal = self.number_of_females(age - 1)
		
		# recovery of value 84
		_tmpVal84 = self.number_of_females(84)
		
		# retrieve param a0 for age i
		_tmpA0 = self.param_a0(age)
		# retrieve param a0 for age 84
		_tmpA084 = self.param_a0(84)
		
		# retrieve param a1 for age i
		_tmpA1 = self.param_a1(age)
		# retrieve param a1 for age 84
		_tmpA184 = self.param_a1(84)
		
		if age == 1:
			_tmpRes = _tmpA0 + _tmpA1 * math.log10(100 - self.life_expectancy)
			_newVal = _tmpVal - _tmpVal * (math.pow(10, _tmpRes) / 1000)
		elif 2 <= age < 5:
			_tmpRes = 1 - math.exp(
				0.25 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 5 <= age <= 84:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA0 + _tmpA1 * math.log10(100 - self.life_expectancy)) / 1000))
			_newVal = _tmpVal - _tmpVal * _tmpRes
		elif 85 <= age <= 89:
			_tmpRes = 1 - math.exp(
				0.20 * math.log(1 - math.pow(10, _tmpA084 + _tmpA184 * math.log10(100 - self.life_expectancy)) / 1000))
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
		
	def update_fertility(self):
		self.currentFertilityParam = 17.22  # self.number_of_children_per_women
	
	def iterate(self):
		
		self.update_fertility()
		
		total_babies = 0
		old_total_population = 0
		total_population = 0
		
		_maxH = 0  # reset the number of men
		_maxF = 0  # female count reset
		
		for age in reversed(range(1, 100)):
			# calculate the number of babies
			number_of_females_in_age = self.number_of_females(age)
			fertility_in_age = self.fertility(age + 1)
			total_babies_of_age = self.calculate_babies(fertility_in_age, number_of_females_in_age)
			# print("number_of_females: ", number_of_females_in_age)
			# print("babies per age: ", total_babies_of_age)
			
			total_babies += total_babies_of_age
			
			_oldTotalHData = self.number_of_males(age)
			_oldTotalFData = self.number_of_females(age)
			
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
			self.set_number_of_males(age, _yearHData)
			self.set_number_of_females(age, _yearFData)
		
		# addition of the past total population of old newborns
		old_total_population += self.number_of_males(0)
		old_total_population += self.number_of_females(0)
		
		print('--- debug ---')
		print(' total babies: ', int(total_babies))
		print(' total_population: ', int(total_population))
		print(' old_total_population: ', old_total_population)
		
		male_babies = total_babies * (self.boys_ratio / 100.0)
		female_babies = total_babies * (1.0 - (self.boys_ratio / 100.0))
		
		if male_babies >= _maxH:
			_maxH = male_babies
		if female_babies >= _maxF:
			_maxF = female_babies
		
		self.set_number_of_males(0, male_babies)
		self.set_number_of_females(0, female_babies)


if __name__ == '__main__':
	sim = Simulation()
	sim.print_curve(2019)
	# sim.show_chart(2019)

	sim.iterate()
	sim.print_curve(2020)
	sim.show_chart(2020)

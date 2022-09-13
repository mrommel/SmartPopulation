
class SimulationRecord:
	def __init__(self, age, men, women):
		self.age = age
		self.men = men
		self.women = women


class SimulationData:
	"""
	age distribution data of the simulation
	"""
	
	def __init__(self):
		"""
		default constructor
		"""
		self.data = []
		
		for age in range(0, 99):
			self.data.append(SimulationRecord(age, 0, 0))
	
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


class SimulationDataGermany2019(SimulationData):
	"""
	https://service.destatis.de/bevoelkerungspyramide/#! from 2019 for germany
	"""
	
	def __init__(self):
		super().__init__()
		
		self.data = []  # remove all existing data rows
		
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

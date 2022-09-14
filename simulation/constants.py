"""simulation constants module."""

# Table of fertility
mapping_fertility = {
	0: 0.0000,
	1: 0.0625,
	2: 0.1259,
	3: 0.1927,
	4: 0.2642,
	5: 0.3407,
	6: 0.4221,
	7: 0.5083,
	8: 0.5990,
	9: 0.6941,
	
	10: 0.7934,
	11: 0.8967,
	12: 1.0039,
	13: 1.1148,
	14: 1.2291,
	15: 1.3468,
	16: 1.4676,
	17: 1.5915,
	18: 1.7183,
	19: 1.8479,
	20: 1.9802,
	
	21: 2.1151,
	22: 2.2524,
	23: 2.3921,
	24: 2.5340,
	25: 2.6782,
	26: 2.8245,
	27: 2.9729,
	28: 3.1232,
	29: 3.2755,
	30: 3.4296,
	
	35: 4.3300,
	40: 5.1900,
	45: 6.0800,
	50: 7.0000,
	55: 7.9500,
	60: 8.9200,
	65: 9.9200,
	70: 10.9300,
	75: 11.9700,
	80: 13.0200,
	85: 14.0900,
	90: 15.1700
}

"""
# Tableau des esperance de vie.
esperance = {
	'10': '4.98',
	'15': '9.64',
	'20': '14.97',
	'25': '20.79',
	'30': '26.91',
	
	'35': '33.13',
	'40': '39.29',
	'45': '45.24',
	'50': '50.87',
	'55': '56.10',
	'60': '60.90',
	
	'65': '65.23',
	'70': '69.12',
	'75': '72.60',
	'80': '75.74',
	'85': '78.63',
	'90': '81.42',
	
	'95': '84.45',
	'96': '85.16',
	'97': '85.95',
	'98': '86.87',
	'99': '88.08',
	'99.5': '88.95',
	'99.8': '88.78',
	'99.9': '90.24'
};
"""

# Tableau a0.
param_a0 = {
	0: -2.16583,
	1: -5.51465,
	2: -5.51465,
	3: -5.51465,
	4: -5.51465,
	5: -4.39268,
	6: -4.39268,
	7: -4.39268,
	8: -4.39268,
	9: -4.39268,
	
	10: -3.69225,
	11: -3.69225,
	12: -3.69225,
	13: -3.69225,
	14: -3.69225,
	15: -2.94252,
	16: -2.94252,
	17: -2.94252,
	18: -2.94252,
	19: -2.94252,
	
	20: -2.74829,
	21: -2.74829,
	22: -2.74829,
	23: -2.74829,
	24: -2.67206,
	25: -2.67206,
	26: -2.67206,
	27: -2.67206,
	28: -2.67206,
	29: -2.51872,
	
	30: -2.51872,
	31: -2.51872,
	32: -2.51872,
	33: -2.51872,
	34: -2.18575,
	35: -2.18575,
	36: -2.18575,
	37: -2.18575,
	38: -2.18575,
	39: -2.67206,
	
	40: -1.64691,
	41: -1.64691,
	42: -1.64691,
	43: -1.64691,
	44: -1.64691,
	45: -0.93877,
	46: -0.93877,
	47: -0.93877,
	48: -0.93877,
	49: -0.93877,
	
	50: -0.38269,
	51: -0.38269,
	52: -0.38269,
	53: -0.38269,
	54: -0.38269,
	55: 0.04832,
	56: 0.04832,
	57: 0.04832,
	58: 0.04832,
	59: 0.04832,
	
	60: 0.48768,
	61: 0.48768,
	62: 0.48768,
	63: 0.48768,
	64: 0.48768,
	65: 0.93302,
	66: 0.93302,
	67: 0.93302,
	68: 0.93302,
	69: 0.93302,
	
	70: 1.32649,
	71: 1.32649,
	72: 1.32649,
	73: 1.32649,
	74: 1.32649,
	75: 1.82189,
	76: 1.82189,
	77: 1.82189,
	78: 1.82189,
	79: 1.82189,
	
	80: 2.29,
	81: 2.29,
	82: 2.29,
	83: 2.29,
	84: 2.29,
	85: 2.29,
	86: 2.29,
	87: 2.29,
	88: 2.29,
	89: 2.29,
	
	90: 2.29,
	91: 2.29,
	92: 2.29,
	93: 2.29,
	94: 2.29,
	95: 2.29,
	96: 2.29,
	97: 2.29,
	98: 2.29,
	99: 2.29,
	
	100: 2.29
}

# Tableau a1.
param_a1 = {
	0: 2.4914,
	1: 4.30613,
	2: 4.30613,
	3: 4.30613,
	4: 4.30613,
	5: 3.34845,
	6: 3.34845,
	7: 3.34845,
	8: 3.34845,
	9: 3.34845,
	
	10: 2.83824,
	11: 2.83824,
	12: 2.83824,
	13: 2.83824,
	14: 2.83824,
	15: 2.51152,
	16: 2.51152,
	17: 2.51152,
	18: 2.51152,
	19: 2.51152,
	
	20: 2.47996,
	21: 2.47996,
	22: 2.47996,
	23: 2.47996,
	24: 2.47996,
	25: 2.45176,
	26: 2.45176,
	27: 2.45176,
	28: 2.45176,
	29: 2.45176,
	
	30: 2.38134,
	31: 2.38134,
	32: 2.38134,
	33: 2.38134,
	34: 2.38134,
	35: 2.21784,
	36: 2.21784,
	37: 2.21784,
	38: 2.21784,
	39: 2.21784,
	
	40: 1.94409,
	41: 1.94409,
	42: 1.94409,
	43: 1.94409,
	44: 1.94409,
	45: 1.58125,
	46: 1.58125,
	47: 1.58125,
	48: 1.58125,
	49: 1.58125,
	
	50: 1.32476,
	51: 1.32476,
	52: 1.32476,
	53: 1.32476,
	54: 1.32476,
	55: 1.15017,
	56: 1.15017,
	57: 1.15017,
	58: 1.15017,
	59: 1.15017,
	
	60: 0.98232,
	61: 0.98232,
	62: 0.98232,
	63: 0.98232,
	64: 0.98232,
	65: 0.81446,
	66: 0.81446,
	67: 0.81446,
	68: 0.81446,
	69: 0.81446,
	
	70: 0.67993,
	71: 0.67993,
	72: 0.67993,
	73: 0.67993,
	74: 0.67993,
	75: 0.47414,
	76: 0.47414,
	77: 0.47414,
	78: 0.47414,
	79: 0.47414,
	
	80: 0.2735,
	81: 0.2735,
	82: 0.2735,
	83: 0.2735,
	84: 0.2735,
	85: 0.2735,
	86: 0.2735,
	87: 0.2735,
	88: 0.2735,
	89: 0.2735,
	
	90: 0.2735,
	91: 0.2735,
	92: 0.2735,
	93: 0.2735,
	94: 0.2735,
	95: 0.2735,
	96: 0.2735,
	97: 0.2735,
	98: 0.2735,
	99: 0.2735,
	
	100: 0.2735
}

# Tableau k - fertility per age
param_k = {
	0: 0,
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0,
	6: 0,
	7: 0,
	8: 0,
	9: 0,
	
	10: 0,
	11: 0,
	12: 0,
	13: 0,
	14: 0,
	15: 0.1,
	16: 0.3,
	17: 0.5,
	18: 0.6,
	19: 0.7,
	
	20: 0.8,
	21: 0.9,
	22: 1,
	23: 1,
	24: 1,
	25: 1,
	26: 1,
	27: 1,
	28: 1,
	29: 1,
	
	30: 0.93,
	31: 0.93,
	32: 0.85,
	33: 0.85,
	34: 0.85,
	35: 0.68,
	36: 0.68,
	37: 0.68,
	38: 0.68,
	39: 0.68,
	
	40: 0.35,
	41: 0.35,
	42: 0.35,
	43: 0.35,
	44: 0.35,
	45: 0.05,
	46: 0.05,
	47: 0.05,
	48: 0.05,
	49: 0.05,
	
	50: 0,
	51: 0,
	52: 0,
	53: 0,
	54: 0,
	55: 0,
	56: 0,
	57: 0,
	58: 0,
	59: 0,
	
	60: 0,
	61: 0,
	62: 0,
	63: 0,
	64: 0,
	65: 0,
	66: 0,
	67: 0,
	68: 0,
	69: 0,
	
	70: 0,
	71: 0,
	72: 0,
	73: 0,
	74: 0,
	75: 0,
	76: 0,
	77: 0,
	78: 0,
	79: 0,
	
	80: 0,
	81: 0,
	82: 0,
	83: 0,
	84: 0,
	85: 0,
	86: 0,
	87: 0,
	88: 0,
	89: 0,
	90: 0,
	
	91: 0,
	92: 0,
	93: 0,
	94: 0,
	95: 0,
	96: 0,
	97: 0,
	98: 0,
	99: 0,
	
	100: 0
}

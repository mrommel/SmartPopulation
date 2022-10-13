"""
    state housing policy
"""
from simulation.base import SimulationCategory, PolicyBase, Effect


class StateHousingPolicy(PolicyBase):
	"""
		state housing policy
	"""

	def __init__(self):
		super().__init__(
			"State Housing",
			"Some citizens prefer to own their own homes, but the cost of housing is such that a large proportion of "
			"the population live in rented accommodation. State housing is provided, at a reduced rate, to those who "
			"cannot afford to pay the market rate. This can be expensive to fund, but the social benefits are also "
			"significant.",
			category=SimulationCategory.welfare,
			slider=['NONE', 'LOW', 'MEDIUM', 'HIGH', 'MAXIMUM'],
			can_be_cancelled=True,
			introduce=20,  # in political capital
			cancel=20,  # in political capital
			raise_cost=10,  # in political capital
			lower_cost=10,  # in political capital
			min_cost=1000,
			max_cost=8400,
			implementation=16,
			min_income=0,
			max_income=0
		)

		self.cost_multiplier = []  # _default_,1.0;Health,0.2*(x^6)

		# https://github.com/Thalassicus/Democracy-3/blob/d7d51b848675cae9d6a7a193e040b2f01a83d463/data/missions/germany/germany.txt
		self.slider_value = 'MEDIUM'
		self.value = 0.7

		# connections:
		self.effects.append(Effect('capitalist_mood', '-0.02 - (0.1 * x)'))
		self.effects.append(Effect('poor_mood', '0.05 + (0.05 * x)'))
		self.effects.append(Effect('equality', '0.0 + (0.2 * x)'))
		self.effects.append(Effect('socialist_mood', '0.0 + (0.20 * x)'))
		self.effects.append(Effect('poverty_rate', '0.0 - (0.17 * x)'))
		self.effects.append(Effect('_low_income', '0.0 + (0.17 * x)'))
		# _global_socialism, 0.015 + (0.02 * x), 12
		self.effects.append(Effect('private_housing', '0.0 - (0.8 * x)', 4))
		self.effects.append(Effect('homelessness', '0.0 - (0.4 * x)'))

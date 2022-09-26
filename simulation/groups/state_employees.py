"""
	group of state employees
"""
from simulation.base import GroupBase


class StateEmployeesGroup(GroupBase):
	"""
		group of state employees
	"""
	
	def __init__(self):
		super().__init__(
			'State Employees	',
			'This group covers a wide range of occupations, where people are directly or indirectly working for the '
			'state, whether it be as teachers or doctors in public schools and hospitals, members of the armed forces, '
			'and of course the police force. Unlike people working in the free market, state employees can see a '
			'direct link between the government and their salary and conditions of work. They can be a powerful '
			'political group.',
			0.0,  # mood
			0.0  # freq
		)

		# influences
		# SelfEmployed,-1.0

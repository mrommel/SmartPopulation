"""
	group of parents people
"""
from simulation.base import GroupBase


class ParentsGroup(GroupBase):
	"""
		group of parents people
	"""
	
	def __init__(self):
		super().__init__(
			'Parents',
			'Of course a very high proportion of your citizens are parents, and generally they aren\'t people who vote '
			'as a group, but there are some topics, such as childcare provision and education where the government has '
			'to consider the impact on them as a group.',
			0.0,  # mood
			0.24  # freq
		)

		# influences
		# Retired, -1.0
	
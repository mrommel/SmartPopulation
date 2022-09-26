"""
	group of middle income people
"""
from simulation.base import GroupBase


class MiddleIncomeGroup(GroupBase):
	"""
		group of middle income people
	"""
	
	def __init__(self):
		super().__init__(
			'Middle Income',
			'Neither poor, nor wealthy, the average middle income earner works most of his life to pay for his or her '
			'house, probably can afford a good holiday each year and may own one or more cars. Middle income earners '
			'are often very sensitive to changes in income tax. They usually make up a large proportion of the voting '
			'population.',
			0.27,  # mood
			0.41  # freq
		)

		# influences
		# none

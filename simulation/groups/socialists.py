"""
	group of socialist people
"""
from simulation.base import GroupBase


class SocialistGroup(GroupBase):
	"""
		group of socialist people
	"""
	
	def __init__(self):
		super().__init__(
			'Socialist',
			'Socialists are firm believers in the redistribution of wealth. Those who are successful and highly paid '
			'should be heavily taxed so as to provide a better quality of life to those less fortunate. Socialists '
			'believe in a large role for the state in providing universally available services such as free healthcare '
			'for all, free education and heavily subsidized housing and public transport.',
			-0.3,  # mood
			0.1  # freq
		)

"""
	group of wealthy people
"""
from simulation.base import GroupBase


class WealthyGroup(GroupBase):
	"""
		group of wealthy people
	"""
	
	def __init__(self):
		super().__init__(
			'Wealthy',
			'Some people in this group are rich through their own endeavors, others have inherited their wealth. This '
			'is a group of people who have a strong interest in certain tax issues, and will take their own financial '
			'interests into account when voting to a lesser or greater extent. It\'s worth noting that many people '
			'aspire to be more wealthy than they are, and thus taxing the wealthy can be unpopular, even with those '
			'not yet in this group.',
			0.0,  # mood
			0.09  # freq
		)

		# influences
		# none

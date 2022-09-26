"""
	group of young people
"""
from simulation.base import GroupBase


class YoungGroup(GroupBase):
	"""
		group of young people
	"""
	
	def __init__(self):
		super().__init__(
			'Youth',
			'This group represents citizens who are old enough to vote, but still considered young. They will either '
			'still be in further education, or have recent memories of school/university so will be more strongly '
			'affected by those policies affecting education.	',
			0.0,  # mood
			0.17  # freq
		)

		# influences
		# Retired,-1.0
		# Environmentalist,0.15
	
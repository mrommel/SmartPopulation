"""
	group of all people
"""
from simulation.base import GroupBase


class AllGroup(GroupBase):
	"""
		group of all people
	"""
	
	def __init__(self):
		super().__init__(
			'Everyone',
			'A general group representing the interests of society as a whole, with opinions not related to a '
			'particular age group, gender or occupation.',
			0.0,  # mood
			1.0  # freq
		)

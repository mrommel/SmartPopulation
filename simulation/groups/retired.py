"""
	group of retired people
"""
from simulation.base import GroupBase


class RetiredGroup(GroupBase):
	"""
		group of retired people
	"""
	
	def __init__(self):
		super().__init__(
			'Retired',
			'Retired people don’t have to worry about schools, commuting to work and working conditions, but they are '
			'naturally very interested in the level of pension provision. Retired people can be a formidable political '
			'enemy if angered, because they have ample time on their hands to campaign against you.	',
			0.0,  # mood
			0.19  # freq
		)

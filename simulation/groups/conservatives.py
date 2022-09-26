"""
	group of conservatives people
"""
from simulation.base import GroupBase


class ConservativesGroup(GroupBase):
	"""
		group of conservatives people
	"""
	
	def __init__(self):
		super().__init__(
			'Conservatives',
			'Conservatives are believers in traditional family values, no sex before marriage, strong policies on law '
			'and order and are against the legalization of drugs. They are generally in favor of strong policies on '
			'law and order.',
			0.0,  # mood
			0.24  # freq
		)
		
		# influences
		# Religious,0.25
		# Environmentalist,-0.1



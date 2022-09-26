"""
	group of patriot people
"""
from simulation.base import GroupBase


class PatriotGroup(GroupBase):
	"""
		group of patriot people
	"""
	
	def __init__(self):
		super().__init__(
			'Patriot',
			'Most people claim to be patriots when asked, but there is a small proportion of any population who hold '
			'strong views about your countries position in the world and also its defense. Patriots are passionate '
			'about putting your country first and keeping an adequate military, even in times of peace.	',
			0.0,  # mood
			0.1  # freq
		)

		# influences
		# EthnicMinorities,-0.2

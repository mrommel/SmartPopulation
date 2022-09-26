"""
	group of religious people
"""
from simulation.base import GroupBase


class ReligiousGroup(GroupBase):
	"""
		group of religious people
	"""
	
	def __init__(self):
		super().__init__(
			'Religious',
			'Although there is a wide range of different religions, most of the larger organized groups can agree on a '
			'few basic principles. Religious voters support religious teaching in schools, specialized \'faith\' '
			'schools, and are also pro marriage. Religious groups may also be concerned by abortion and organ '
			'donation, and are unlikely to be pro-science.',
			0.0,  # mood
			0.05  # freq
		)

		# influences
		# none
	
"""
	group of commuters
"""
from simulation.base import GroupBase


class CommuterGroup(GroupBase):
	"""
		group of commuters
	"""
	
	def __init__(self):
		super().__init__(
			'Commuter',
			'Commuters are people who have to travel a fair distance from home to work each day. Some people commute '
			'by car, others by rail, bus or subway. Although its not a traditional political issue, commuting is '
			'unpopular, and people who commute each day can be made very unhappy by traffic congestion, high fuel '
			'prices (for drivers) and inefficient transport systems.',
			0.0,  # mood
			0.7  # freq
		)

		# influences
		# Retired,-1.0
	
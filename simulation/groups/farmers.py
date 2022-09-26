"""
	group of farmers
"""
from simulation.base import GroupBase


class FarmersGroup(GroupBase):
	"""
		group of farmers
	"""
	
	def __init__(self):
		super().__init__(
			'Farmers',
			'A proportion of the population still works on the land to provide food. Although food can be imported, '
			'most governments are aware of the strategic advantage to have sufficient food grown within your own '
			'borders. As a result, farmers are often given hefty subsidies and in some cases even encouraged to '
			'overproduce. Farmers can be a very vocal and very powerful political group.',
			0.0,  # mood
			0.08  # freq
		)

		# influences
		# Commuter,-1.0
		# Retired,-1.0
	
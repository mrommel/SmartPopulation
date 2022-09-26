"""
	group of trade unionists
"""
from simulation.base import GroupBase


class TradeUnionistGroup(GroupBase):
	"""
		group of trade unionists
	"""
	
	def __init__(self):
		super().__init__(
			'Trade Unionist	',
			'Many employees are members of trade unions, although not all consider themselves to be active trade '
			'unionists. Although on the surface, trade unions are only concerned with their members wages and working '
			'conditions, trade unionists tend towards agreement on most areas of left wing and liberal politics.',
			-0.25,  # mood
			0.2  # freq
		)

		# influences
		# SelfEmployed,-1.0
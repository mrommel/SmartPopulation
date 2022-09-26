"""
	group of self-employed people
"""
from simulation.base import GroupBase


class SelfEmployedGroup(GroupBase):
	"""
		group of self-employed people
	"""
	
	def __init__(self):
		super().__init__(
			'Self Employed	',
			'People who work for themselves are very sensitive to a number of economic factors. Those who do well are '
			'naturally keen to profit from their endeavors without paying too much in tax, and are sensitive to '
			'over-regulation, especially considering employment. Even though few small businessmen become rich, '
			'they are still concerned by any threat of high taxes levied on the successful.',
			0.0,  # mood
			0.15  # freq
		)

		# influences
		# StateEmployees,-1.0
		# TradeUnionist,-1.0
		# Retired,-1.0
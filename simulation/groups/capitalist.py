"""
	group of capitalists
"""
from simulation.base import GroupBase


class CapitalistGroup(GroupBase):
	"""
		group of capitalists
	"""
	
	def __init__(self):
		super().__init__(
			'Capitalist',
			'Capitalists are strong believers in the efficiency of market forces. According to capitalists, The system '
			'works best when those who work hard are allowed to profit highly from their endeavors. Capitalists are '
			'opposed to taxation, especially progressive taxation, as it acts as a disincentive to enterprise. Welfare '
			'payments are also seen as a disincentive to free enterprise as they discourage people from working '
			'hard.',
			0.16,  # mood
			0.25  # freq
		)

		# influences
		# TradeUnionist,-0.25
		# SelfEmployed,0.2



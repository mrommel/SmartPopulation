"""
	group of environmentalists
"""
from simulation.base import GroupBase


class EnvironmentalistGroup(GroupBase):
	"""
		group of environmentalists
	"""
	
	def __init__(self):
		super().__init__(
			'Environmentalist',
			'Environmentalists (also known as greens) have views on a wide range of topics, including transport, '
			'air pollution, energy sources, taxation, food production and recycling. Environmentalists are a very '
			'vocal political group, and can be a very loyal friend or bitter enemy of the government.',
			0.2,  # mood
			0.09  # freq
		)
		
		# influences
		# Motorist,-0.2

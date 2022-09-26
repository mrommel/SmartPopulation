"""
	group of motorists
"""
from simulation.base import GroupBase


class MotoristGroup(GroupBase):
	"""
		group of motorists
	"""
	
	def __init__(self):
		super().__init__(
			'Motorist',
			'Motorists wouldn\'t consider themselves a conventional political group, but they are so numerous and so '
			'easily influenced by policies such as car tax, fuel tax and road building, that the government is wise to '
			'keep an eye on their views. Motorists can even be supportive of subsidies to other forms of transport, '
			'if these mean less congested and faster roads for themselves.	',
			0.0,  # mood
			0.32  # freq
		)

		# influences
		# Environmentalist,-0.2
	
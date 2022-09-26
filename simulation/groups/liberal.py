"""
	group of liberal people
"""
from simulation.base import GroupBase


class LiberalGroup(GroupBase):
	"""
		group of liberal people
	"""
	
	def __init__(self):
		super().__init__(
			'Liberal',
			'At its heart, the liberal political group defines people who believe strongly in personal liberty and '
			'freedom. This includes freedom from unwarranted monitoring or intrusion by the state. Liberals are also '
			'strong supporters of human rights, such as the right to a fair trial, right to personal privacy etc. '
			'Liberals are often characterized as the opposite of the religious right.',
			0.0,  # mood
			0.27  # freq
		)
		
		# influences
		# Religious,-0.2
		# Environmentalist,0.1
	
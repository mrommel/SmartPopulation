"""
	group of poor people
"""
from simulation.base import GroupBase


class PoorGroup(GroupBase):
	"""
		group of poor people
	"""
	
	def __init__(self):
		super().__init__(
			'Poor',
			'Poor people are naturally far more dependent on welfare payments from the state than anybody else. They '
			'may also be worried about unemployment more than most, as they consider their jobs more vulnerable. Poor '
			'people also are in favor of any progressive tax system that redistributes money their way, such as taxes '
			'on luxury goods.',
			0.0,  # mood
			0.25  # freq
		)

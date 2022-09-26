"""
	group of people of ethnic minorities
"""
from simulation.base import GroupBase


class EthnicMinoritiesGroup(GroupBase):
	"""
		group of people of ethnic minorities
	"""
	
	def __init__(self):
		super().__init__(
			'Ethnic Minorities',
			'A group representing everyone who is not in the majority ethnic group for this country. They may be '
			'immigrants, or may be born to immigrants, and will have strong views regarding foreign aid and border '
			'controls, as well as racial discrimination.',
			0.0,  # mood
			0.3  # freq
		)

		# influences
		# Patriot,-0.2
	
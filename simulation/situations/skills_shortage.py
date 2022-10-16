"""
	situation of skills shortage
"""
from simulation.base import SituationBase, SimulationCategory, Effect


class SkillsShortageSituation(SituationBase):
	"""
		situation of skills shortage
	"""
	
	def __init__(self):
		super().__init__(
			'Skills Shortage',
			'Businesses tell us that they simply can not find enough skilled and trained people to employ. The modern '
			'economy is increasingly skills-based and our citizens just aren\'t educated enough to take their place in '
			'the modern workforce. This is going to have a negative impact on the economy.',
			'Business leaders have complained that we simply do not have enough highly skilled workers to fill job vacancies.',
			'Business leaders inform you that there is no longer a noticeable skills shortage in the economy. Our '
			'citizens are now sufficiently educated and trained to provide for the economies needs.',
			SimulationCategory.economy,
			0.75,  # default
			0.6,
			0.4
		)
		
		# input @todo move to each simulation inputs
		# AdultEducationSubsidies,0-(0.2*x),8	 # skills_shortage
		# UniversityGrants,0-(0.2*x)	# skills_shortage
		
		# effects
		self.effects.append(Effect('gdp', '0.0 - (0.44 * x) ** 1.4'))

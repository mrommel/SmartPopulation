"""immigration simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class ImmigrationSimulation(SimulationBase):
	"""
		immigration simulation
	"""
	
	def __init__(self):
		super().__init__(
			"Immigration",
			"Immigration measures the number of people entering this country, both legally and illegally, "
			"with the intent of making this their new home. Immigration is generally caused by a strong economy, "
			"as those living in poorer countries seek out employment and a higher standard of living. Immigration can "
			"be reduced by border controls, and citizenship tests. Too much immigration too fast can lead to racial "
			"tensions developing.",
			SimulationCategory.foreign_policy,
			'simulation_immigration.png',
			1.0,
			emotion=SimulationEmotion.unknown
		)
		
		# connections:
		self.effects.append(Effect('racial_tension', '1.4 * (x ** 3)', 8))
		self.effects.append(Effect('unemployment', '0.3 * (x ** 3)', 2))
		self.effects.append(Effect('gdp', '-0.035 + (0.035 * x)'))
		self.effects.append(Effect('ethnic_minorities_freq', '-0.7 + (1.4 * x)', 8))
		self.effects.append(Effect('wages', '-0.0 - (0.22 * x)'))
		# StateHealthService_cost, 0 + (0.07 * x)
		# StateHousing_cost, 0 + (0.07 * x)
		self.effects.append(Effect('homelessness', '0.0 + (0.06 * x)', 4))
		self.effects.append(Effect('skills_shortage', '0.0 - (0.2 * x)'))
	
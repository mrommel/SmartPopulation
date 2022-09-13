import unittest

from simulation.configuration import SimulationConfiguration
from simulation.simulation import Simulation


class TestSimulation(unittest.TestCase):
	
	def test_basic_population(self):
		# GIVEN
		config = SimulationConfiguration()
		sim = Simulation(config)
		population_before = sim.population
		
		# WHEN
		pass

		# THEN
		population_after = sim.population
		self.assertEqual(population_after, population_before)
	
	def test_population_increases(self):
		# GIVEN
		config = SimulationConfiguration(81.8, 3.5)  # number_of_children_per_women must bigger than usual
		sim = Simulation(config)
		population_before = sim.population
		
		# WHEN
		sim.iterate()

		# THEN
		population_after = sim.population
		self.assertGreater(population_after, population_before)


if __name__ == '__main__':
	unittest.main()

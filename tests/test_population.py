import unittest

from population.configuration import PopulationConfiguration, PopulationConfigurationGermany2019
from population.data import SimulationDataGermany2019, SimulationData
from population.population import Population
from simulation.simulation import Simulation


class TestPopulation(unittest.TestCase):
	
	def test_set_males(self):
		# GIVEN
		config = PopulationConfigurationGermany2019()
		data = SimulationData()
		sim = Population(config=config, data=data)
		population_before = sim.population
		
		# WHEN
		sim.data.set_number_of_males(25, 2000)
		
		# THEN
		population_after = sim.population
		self.assertEqual(population_before, 0)
		self.assertEqual(population_after, 2000)
	
	def test_set_females(self):
		# GIVEN
		config = PopulationConfigurationGermany2019()
		data = SimulationData()
		sim = Population(config=config, data=data)
		population_before = sim.population
		
		# WHEN
		sim.data.set_number_of_females(25, 3000)
		
		# THEN
		population_after = sim.population
		self.assertEqual(population_before, 0)
		self.assertEqual(population_after, 3000)
	
	def test_basic_population(self):
		# GIVEN
		config = PopulationConfigurationGermany2019()
		data = SimulationDataGermany2019()
		sim = Population(config=config, data=data)
		population_before = sim.population
		
		# WHEN
		pass
		
		# THEN
		population_after = sim.population
		self.assertEqual(population_after, population_before)
	
	def test_population_increases(self):
		# GIVEN
		config = PopulationConfiguration(81.8, 3.5)  # number_of_children_per_women must bigger than usual
		data = SimulationDataGermany2019()
		sim = Population(config=config, data=data)
		population_before = sim.population
		
		# WHEN
		sim.iterate()
		
		# THEN
		population_after = sim.population
		self.assertGreater(population_after, population_before)


if __name__ == '__main__':
	unittest.main()

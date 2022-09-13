from simulation.configuration import SimulationConfiguration, SimulationConfigurationGermany2019
from simulation.data import SimulationDataGermany2019
from simulation.simulation import Simulation

if __name__ == '__main__':
	config = SimulationConfigurationGermany2019()
	data = SimulationDataGermany2019()
	sim = Simulation(config=config, data=data)
	# sim.print_curve(2019)
	# sim.show_chart(2019)
	
	for year in range(2020, 2100):
		sim.iterate()
		print('population:', sim.population, 'in', year)
# sim.print_curve(2020)
# sim.show_chart(2020)

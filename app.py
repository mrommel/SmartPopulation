from simulation.configuration import SimulationConfiguration
from simulation.simulation import Simulation

if __name__ == '__main__':
	config = SimulationConfiguration()
	sim = Simulation(config)
	# sim.print_curve(2019)
	# sim.show_chart(2019)
	
	for year in range(2020, 2100):
		sim.iterate()
		print('population:', sim.population, 'in', year)
	# sim.print_curve(2020)
	# sim.show_chart(2020)

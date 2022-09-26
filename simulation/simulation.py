""" simulation """
from simulation.groups.all import AllGroup
from simulation.groups.conservatives import ConservativesGroup
from simulation.groups.environmentalists import EnvironmentalistGroup
from simulation.groups.liberal import LiberalGroup
from simulation.groups.middle_income import MiddleIncomeGroup
from simulation.groups.patriot import PatriotGroup
from simulation.groups.poor import PoorGroup
from simulation.groups.retired import RetiredGroup
from simulation.groups.socialists import SocialistGroup
from simulation.policies.armed_police import ArmedPolicePolicy
from simulation.policies.policy_force import PoliceForcePolicy
from simulation.simulations.air_travel import AirTravelSimulation
from simulation.simulations.bus_usage import BusUsageSimulation
from simulation.simulations.car_usage import CarUsageSimulation
from simulation.simulations.co2_emissions import CO2EmissionsSimulation
from simulation.simulations.energy_efficiency import EnergyEfficiencySimulation
from simulation.simulations.environment import EnvironmentSimulation
from simulation.simulations.average_income import AverageIncomeSimulation
from simulation.simulations.crime_rate import CrimeRateSimulation
from simulation.simulations.education import EducationSimulation
from simulation.simulations.equality import EqualitySimulation
from simulation.simulations.foreign_relations import ForeignRelationsSimulation
from simulation.simulations.gdp import GDPSimulation
from simulation.simulations.health import HealthSimulation
from simulation.simulations.immigration import ImmigrationSimulation
from simulation.simulations.international_trade import InternationalTradeSimulation
from simulation.simulations.lifespan import LifespanSimulation
from simulation.simulations.low_income import LowIncomeSimulation
from simulation.simulations.middle_income import MiddleIncomeSimulation
from simulation.simulations.oil_demand import OilDemandSimulation
from simulation.simulations.oil_price import OilPriceSimulation
from simulation.simulations.poverty import PovertySimulation
from simulation.simulations.racial_tension import RacialTensionSimulation
from simulation.simulations.rail_usage import RailUsageSimulation
from simulation.simulations.technology import TechnologySimulation
from simulation.simulations.terrorism import TerrorismSimulation
from simulation.simulations.tourism import TourismSimulation
from simulation.simulations.unemployment import UnemploymentSimulation
from simulation.simulations.violent_crime_rate import ViolentCrimeRateSimulation
from simulation.simulations.wages import WagesSimulation
from simulation.simulations.worker_productivity import WorkerProductivitySimulation
from simulation.simulations.working_week import WorkingWeekSimulation
from simulation.situations.alcoholism import AlcoholismSituation
from simulation.situations.homelessness import HomelessnessSituation
from simulation.situations.obesity import ObesitySituation
from simulation.situations.organised_crime import OrganisedCrimeSituation
from simulation.situations.pollution import PollutionSituation


class Simulation:
	"""
		simulation
	"""
	
	def __init__(self):
		# people / groups
		self.groups = {
			'socialist': SocialistGroup(),
			# 'capitalist':
			'retired': RetiredGroup(),
			# 'commuter':
			'patriot': PatriotGroup(),
			# 'motorist':
			'liberal': LiberalGroup(),
			# 'religious':
			# 'trade_unionist':
			# 'self_employed':
			'environmentalist': EnvironmentalistGroup(),
			# 'wealthy':
			'poor': PoorGroup(),
			'middle_income': MiddleIncomeGroup(),
			# 'parents':
			# 'farmers':
			# 'state_employees':
			'conservatives': ConservativesGroup(),
			# 'young':
			# 'ethnic_minorities':
			'all': AllGroup(),
		}
		
		# simulations
		self.simulations = {
			'health': HealthSimulation(),
			'lifespan': LifespanSimulation(),
			'education': EducationSimulation(),
			'crime_rate': CrimeRateSimulation(),
			'violent_crime_rate': ViolentCrimeRateSimulation(),
			'poverty_rate': PovertySimulation(),
			'average_income': AverageIncomeSimulation(),  # ??? is this needed ???
			'equality': EqualitySimulation(),
			'environment': EnvironmentSimulation(),
			'working_week': WorkingWeekSimulation(),
			'technology': TechnologySimulation(),
			'car_usage': CarUsageSimulation(),
			'rail_usage': RailUsageSimulation(),
			'bus_usage': BusUsageSimulation(),
			'worker_productivity': WorkerProductivitySimulation(),
			'unemployment': UnemploymentSimulation(),
			'co2_emissions': CO2EmissionsSimulation(),
			'air_travel': AirTravelSimulation(),
			'immigration': ImmigrationSimulation(),
			'energy_efficiency': EnergyEfficiencySimulation(),
			'racial_tension': RacialTensionSimulation(),
			'foreign_relations': ForeignRelationsSimulation(),
			'international_trade': InternationalTradeSimulation(),
			'oil_demand': OilDemandSimulation(),
			# Oil Supply
			'oil_price': OilPriceSimulation(),
			'_terrorism': TerrorismSimulation(),
			'_low_income': LowIncomeSimulation(),  # Poor Earnings
			'_middle_income': MiddleIncomeSimulation(),  # Middle Earnings
			# High Earnings
			'gdp': GDPSimulation(),
			# Private Health Care
			# Private Housing
			# Private Schools
			# Private Pensions
			# Tobacco Usage
			# Alcohol Consumption
			# Traffic Congestion
			'tourism': TourismSimulation(),
			'wages': WagesSimulation(),
			# Legal Drug Consumption
			# Currency Strength
		}
		
		# https://github.com/bakster55/W3JsonToExcel/blob/master/democracy3/data/simulation/situations.csv
		self.situations = {
			'pollution': PollutionSituation(),
			# ...
			'organised_crime': OrganisedCrimeSituation(),
			'alcoholism': AlcoholismSituation(),
			# ...
			'homelessness': HomelessnessSituation(),
			# ...
			'obesity': ObesitySituation(),
		}
		
		# https://github.com/bakster55/W3JsonToExcel/blob/master/democracy3/data/simulation/policies.csv
		self.policies = {
			# AdultEducationSubsidies
			# AgricultureSubsidies
			# AirlineTax
			# AlcoholLaw
			# AlcoholTax
			'armed_police': ArmedPolicePolicy(),
			# BanSundayShopping
			# BiofuelSubsidies
			# BorderControls
			# BusLanes
			# BusSubsidies
			# CarbonTax
			# CarEmmissionsLimits
			# CarTax
			# CCTVCameras
			# ChildBenefit
			# ChildcareProvision
			# CitizenshipTests
			# CleanEnergySubsidies
			# CleanFuelSubsidy
			# CommunityPolicing
			# ConsumerRights
			# CorporationTax
			# Creationism
			# Curfews
			# DeathPenalty
			# DetentionWithoutTrial
			# DisabilityBenefit
			# FaithSchoolSubsidies
			# ForeignAid
			# FreeBusPasses
			# FreeEyeTests
			# FreeSchoolMeals
			# Gambling
			# GatedCommunities
			# GraduateTax
			# HandgunLaws
			# HybridCarsInitiative
			# IDCards
			# ImportTarrifs
			# IncomeTax
			# FlatTax
			# CapitalGainsTax
			# InheritanceTax
			# IntelligenceServices
			# InternetCensorship
			# InternetTax
			# JuryTrial
			# LabourLaws
			# LegalAid
			# LegaliseProstitution
			# LuxuryGoodsTax
			# MarriedTaxAllowance
			# MaternityLeave
			# MicrogenerationGrants
			# MilitarySpending
			# Monorail
			# MortgageTaxRelief
			# Narcotics
			# NationalService
			# OrganDonation
			# OrganicSubsidy
			# PetrolTax
			# PhoneTapping
			# PlasticBagTax
			'policy_force': PoliceForcePolicy(),
			# PollutionControls
			# PrisonerTagging
			# Prisons
			# PropertyTax
			# PublicLibraries
			# RacialProfiling
			# RaceDiscriminationAct
			# RailSubsidies
			# Recycling
			# RoadBuilding
			# RuralDevelopmentGrants
			# SalesTax
			# ...
		}
		
		self.started_situations = []
		self.ended_situations = []
	
	def iterate(self):
		"""
			one iteration of the simulation
			
			:return: (nothing)
		"""
		# -------- prepare --------------
		for _, simulation_item in self.simulations.items():
			simulation_item.prepare()
			
		for _, group_item in self.groups.items():
			group_item.prepare()
			
		for _, situation_item in self.situations.items():
			situation_item.prepare()
			
		for _, policy_item in self.policies.items():
			policy_item.prepare()
		
		# -------- iterate --------------
		for _, simulation_item in self.simulations.items():
			simulation_item.iterate(self)
			
		for _, group_item in self.groups.items():
			group_item.iterate(self)
			
		for _, situation_item in self.situations.items():
			situation_item.iterate(self)
			
		for _, policy_item in self.policies.items():
			policy_item.iterate(self)
		
		# -------- finish --------------
		for _, simulation_item in self.simulations.items():
			simulation_item.finish()
			
		for _, group_item in self.groups.items():
			group_item.finish()
			
		for _, situation_item in self.situations.items():
			situation_item.finish()
			
		for _, policy_item in self.policies.items():
			policy_item.finish()
		
		# -------- show situations --------------
		for started_situation in self.started_situations:
			print(f'situation {started_situation.name} started:')
			print(f'=> {started_situation.start_text}')
		
		for ended_situation in self.ended_situations:
			print(f'situation {ended_situation.name} ended:')
			print(f'=> {ended_situation.end_text}')
			
		self.started_situations = []
		self.ended_situations = []
		
	def print(self):
		"""
			print the summary of this simulation
			
			:return: (nothing)
		"""
		print('---------------------------')
		print('--- simulations -----------')
		for _, simulation_item in self.simulations.items():
			simulation_item.print()
		print('')
		print('--- groups ----------------')
		for _, group_item in self.groups.items():
			group_item.print()
		print('')
		print('--- situations ------------')
		for _, situation_item in self.situations.items():
			situation_item.print()
		
		print('')
		print('---------------------------')
		
		print('')


if __name__ == '__main__':
	simulation = Simulation()
	simulation.print()

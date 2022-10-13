"""private pensions simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class PrivatePensionsSimulation(SimulationBase):
    """
        private pensions simulation
    """

    def __init__(self):
        super().__init__(
            "Private Pensions",
            "The size of the private pension sector. This may run alongside a minimal state pension, or completely "
            "replace it in countries that are happy to leave retirement planning to individuals. Many poor members of "
            "society will not have the means to save adequately for their retirement without state help.	",
            SimulationCategory.welfare,
            'simulation_default.png',
            0.5,
            emotion=SimulationEmotion.high_bad
        )

        # input @todo
        # StatePensions,0-(0.8*x),4
        # GDP,0+(0.5*x),4

        # connections:
        self.effects.append(Effect('_middle_income', '0.0 - (0.10 * x)'))
        self.effects.append(Effect('retired_mood', '0.2 + (0.55 * x)'))
        # self.effects.append(Effect('retired_income, 0.1 + (0.2 * x)'))
        self.effects.append(Effect('capitalist_mood', '0.0 + (0.1 * x)'))

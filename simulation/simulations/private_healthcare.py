"""private healthcare simulation"""
from simulation.base import SimulationCategory, SimulationBase, Effect, SimulationEmotion


class PrivateHealthCareSimulation(SimulationBase):
    """
        private healthcare simulation
    """

    def __init__(self):
        super().__init__(
            "Private HealthCare",
            "The size of the private healthcare sector. This will arise naturally from supply and demand, "
            "and be boosted in boom times, but can be reduced by providing a decent state health care system instead. "
            "The downside with private health care is that the poorest in society can not afford it, and may also "
            "avoid treatment until it becomes essential in order to save costs.	",
            SimulationCategory.welfare,
            'simulation_default.png',
            0.6,
            emotion=SimulationEmotion.high_bad
        )

        # connections:
        self.effects.append(Effect('health', '0.0 + (0.25 * x)', 4))
        self.effects.append(Effect('_low_income', '0.0 - (0.2 * x)', 4))
        self.effects.append(Effect('_middle_income', '0.0 - (0.08 * x)', 4))
        self.effects.append(Effect('retired_mood', '0.0 + (0.16 * x)'))
        self.effects.append(Effect('unemployment', '0.0 - (0.07 * x)'))
        self.effects.append(Effect('trade_unionist_mood', '0.0 - (0.1 * x)'))
        self.effects.append(Effect('capitalist_mood', '0.0 + (0.1 * x)'))
        self.effects.append(Effect('obesity', '-0.2 * (x ** 6)', 12))

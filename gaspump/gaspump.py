import dataclasses
from dataclasses import dataclass
from gasoline.gasoline import (
    Gasoline,
    GasPortion,
)


class NegativeVoltage(ValueError):
    pass


class TooHighVoltage(ValueError):
    pass


@dataclass
class GasPump:
    connected_gas_tank: GasPortion
    max_flow_lps: float  # liters per second

    def apply(
            self,
            voltage: float,
            seconds: float,
    ) -> GasPortion:
        if voltage < 0:
            raise NegativeVoltage
        if voltage > 14:
            raise TooHighVoltage
        flow_lps = self.max_flow_lps * voltage / 12
        volume = round(min(
            self.connected_gas_tank.volume_liters,
            flow_lps * seconds
        ), ndigits=2)
        self.connected_gas_tank.volume_liters -= volume
        return dataclasses.replace(
            self.connected_gas_tank,
            volume_liters=volume
        )

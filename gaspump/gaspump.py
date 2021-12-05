import dataclasses
from dataclasses import dataclass
from typing import Optional

from engine.engine import Engine
from gasoline.gasoline import GasPortion


class NegativeVoltage(ValueError):
    pass


class TooHighVoltage(ValueError):
    pass


@dataclass
class GasPump:
    connected_gas_tank: GasPortion
    connected_engine: Optional[Engine]
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
        gas_portion = dataclasses.replace(
                self.connected_gas_tank,
                volume_liters=volume
            )
        if self.connected_engine is not None:
            self.connected_engine.supply(
                gas_portion=gas_portion,
                seconds=seconds,
            )
        return gas_portion

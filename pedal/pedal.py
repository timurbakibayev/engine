from dataclasses import dataclass

from gasoline.gasoline import GasPortion
from gaspump.gaspump import GasPump


@dataclass
class Pedal:
    connected_gas_pump: GasPump

    def press(
            self,
            how_hard: float,
            seconds: float,
    ) -> GasPortion:
        if seconds < 0:
            raise ValueError("No negative time period allowed")
        how_hard = max(0, how_hard)
        how_hard = min(1, how_hard)
        return self.connected_gas_pump.apply(
            voltage=12*how_hard,
            seconds=seconds,
        )

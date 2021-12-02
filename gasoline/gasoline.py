import dataclasses
from abc import ABC
from dataclasses import dataclass


@dataclass
class Gasoline(ABC):
    octane: float


class UnwantedGasolineMix(ValueError):
    pass


@dataclass
class GasPortion:
    gasoline: Gasoline
    volume_liters: float

    def __add__(self, other:"GasPortion") -> "GasPortion":
        if type(self.gasoline) != type(other.gasoline):
            raise UnwantedGasolineMix
        volume_liters = self.volume_liters + other.volume_liters
        octane = self.gasoline.octane * (self.volume_liters / volume_liters)
        octane += other.gasoline.octane * (other.volume_liters / volume_liters)
        octane = round(octane, ndigits=2)
        return GasPortion(
            gasoline=dataclasses.replace(self.gasoline, octane=octane),
            volume_liters=volume_liters,
        )

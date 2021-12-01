from abc import ABC
from dataclasses import dataclass


class Gasoline(ABC):
    pass


@dataclass
class Benzine(Gasoline):
    octane: int


@dataclass
class Diesel(Gasoline):
    octane: int


@dataclass
class GasPortion:
    gasoline: Gasoline
    volume_liters: float

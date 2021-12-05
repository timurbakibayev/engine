import pytest

from gasoline.gasoline import (
    Gasoline,
    GasPortion,
    UnwantedGasolineMix,
)


class Benzine(Gasoline):
    pass


class Diesel(Gasoline):
    pass


class TestCreateBenzine:
    def test_create_benzine(self) -> None:
        benzine = Benzine(octane=95)
        diesel = Diesel(octane=70)
        assert isinstance(benzine, Gasoline)
        assert isinstance(benzine, Benzine)
        assert isinstance(diesel, Gasoline)
        assert isinstance(diesel, Diesel)

    def test_create_a_portion(self) -> None:
        benzine95 = Benzine(octane=95)
        benzine98 = Benzine(octane=98)
        portion1 = GasPortion(
            gasoline=benzine95,
            volume_liters=2.5,
        )
        assert isinstance(portion1, GasPortion)
        portion2 = GasPortion(
            gasoline=benzine98,
            volume_liters=3.5,
        )
        assert isinstance(portion1, GasPortion)
        mixed = portion1 + portion2
        assert mixed.gasoline.octane == 96.75
        diesel = GasPortion(
            gasoline=Diesel(octane=70),
            volume_liters=100,
        )
        with pytest.raises(UnwantedGasolineMix):
            portion1 + diesel
        with pytest.raises(UnwantedGasolineMix):
            diesel + portion1

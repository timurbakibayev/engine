from gasoline.gasoline import GasPortion, Gasoline
from gaspump.gaspump import GasPump
from pedal.pedal import Pedal


class Benzine(Gasoline):
    pass


class TestPedal:
    def test_gas_pump(self) -> None:
        gas_tank = GasPortion(
            gasoline=Benzine(
                octane=95,
            ),
            volume_liters=10,
        )
        gas_pump = GasPump(
            connected_gas_tank=gas_tank,
            connected_engine=None,
            max_flow_lps=0.2,
        )
        pedal = Pedal(
            connected_gas_pump=gas_pump,
        )

        output_gas = pedal.press(
            how_hard=0.5,
            seconds=5,
        )

        assert output_gas.volume_liters == 0.5

        output_gas = pedal.press(
            how_hard=1,
            seconds=10,
        )

        assert output_gas.volume_liters == 2

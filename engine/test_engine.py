from engine.engine import Engine
from gasoline.gasoline import Gasoline, GasPortion


class Benzine(Gasoline):
    pass


class TestEngine:
    def test_engine(self) -> None:
        benzine95 = Benzine(octane=95)
        benzine100 = Benzine(octane=100)
        engine = Engine(
            gasoline=benzine95,
            max_rpm=1000*60,
            max_flow_speed_lps=1,
        )
        # test full speed
        engine.supply(
            gas_portion=GasPortion(
                gasoline=benzine100,
                volume_liters=1,
            ),
            seconds=1,
        )
        print(engine.rotations)

    def test_standard_engine(self) -> None:
        engine = Engine.produce_a_standard_engine()
        assert isinstance(engine, Engine)

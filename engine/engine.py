from gasoline.gasoline import GasPortion, Gasoline, UnwantedGasolineMix


class Engine:
    def __init__(
            self,
            gasoline: Gasoline,
            max_flow_speed_lps: float = 0.2,
            max_rpm:float = 5000,
    ):
        self.max_flow_speed_lps = max_flow_speed_lps
        self.max_rpm = max_rpm
        self.gasoline = gasoline
        self.total_supplied_gas = GasPortion(
            gasoline=gasoline,
            volume_liters=0,
        )
        self.rotations = 0

    @classmethod
    def produce_a_standard_benzine_engine(cls):
        class Benzine(Gasoline):
            pass

        benzine95 = Benzine(octane=95)
        return cls(
            gasoline=benzine95,
        )

    @classmethod
    def produce_a_standard_diesel_engine(cls):
        class Diesel(Gasoline):
            pass

        diesel70 = Diesel(octane=95)
        return cls(
            gasoline=diesel70,
        )

    def supply(
            self,
            gas_portion: GasPortion,
            seconds: float,
    ):
        if gas_portion.volume_liters <= 0 or seconds <= 0:
            return
        self.total_supplied_gas += gas_portion
        flow_speed = min(
            gas_portion.volume_liters / seconds,
            0.2
        )
        flow_speed_relative = flow_speed / self.max_flow_speed_lps
        octane_relative = gas_portion.gasoline.octane / self.gasoline.octane
        rpm = self.max_rpm * flow_speed_relative * octane_relative
        # now convert rates per minute to rates per second
        rps = rpm / 60
        # and actually rotate the engine:
        self.rotations += rps * seconds

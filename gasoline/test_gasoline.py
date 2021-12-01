from gasoline.gasoline import Gasoline, Benzine, Diesel


class TestCreateBenzine():
    def test_create_benzine(self) -> None:
        benzine = Benzine(octane=95)
        diesel = Diesel(octane=70)
        assert isinstance(benzine, Gasoline)
        assert isinstance(benzine, Benzine)
        assert isinstance(diesel, Gasoline)
        assert isinstance(diesel, Diesel)

    def test_create_a_portion(self) -> None:
        benzine = Benzine(octane=95)
        
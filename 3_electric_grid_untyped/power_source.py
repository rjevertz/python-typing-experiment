import abc


class PowerSource(abc.ABC):
    @property
    @abc.abstractmethod
    def power(self):
        ...

    @abc.abstractmethod
    def simulate_time(self, time: float) -> None:
        ...

    @abc.abstractmethod
    def get_id(self):
        ...

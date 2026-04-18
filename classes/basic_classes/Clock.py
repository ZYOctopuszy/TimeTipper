class Clock:
    __slots__ = ["time", "description", "state"]

    def __init__(
        self, time: str, description: str = "Default Description", state: bool = True
    ):
        self.time: str = time
        self.description: str = description
        self.state: bool = state

    def hours(self) -> int:
        return int(self.time.split(":")[0])

    def minutes(self) -> int:
        return int(self.time.split(":")[1])

    def __repr__(self) -> str:
        return self.time

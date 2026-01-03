class Clock:
    def __init__(self, time: str, description: str = "Default Description", state: bool = True):
        self.time: str = time
        self.description: str = description
        self.state: bool = state

    def __str__(self) -> str:
        return self.time

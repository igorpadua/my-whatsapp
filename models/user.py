class User:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def getName(self) -> str:
        return self._getName

    @getName.setter
    def setName(self, value: str) -> None:
        self._getName = value

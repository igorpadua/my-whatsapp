from user import User

class Message:
    def __init__(self, message: str, user: User) -> None:
        self.message = message
        self.user = user

    @property
    def getMessage(self) -> str:
        return self.message

    @getMessage.setter
    def setMessage(self, value: str) -> None:
        self.message = value

    def __repr__(self) -> str:
        return f"Usuário: {self.user.name} - Mensagem: {self.message}"

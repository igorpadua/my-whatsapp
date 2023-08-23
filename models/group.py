from user import User
from message import Message

class Group:
    users: list[User]
    messages: list[Message]

    def __init__(self, name: str) -> None:
        self.name = name
        self.users = []
        self.messages = []

    @property
    def getName(self) -> str:
        return self.name

    @getName.setter
    def setName(self, value: str) -> None:
        self.name = value

    def addUser(self, user: User) -> None:
        self.users.append(user)

    def addMessage(self, message: Message) -> None:
        self.messages.append(message)

    def getMessages(self) -> list[Message]:
        return self.messages

    def getUsers(self) -> list[User]:
        return self.users

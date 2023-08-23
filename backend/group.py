from user import User
from message import Message
from typing import List

class Group:
    users: List[User]
    messages: List[Message]

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

    def getMessages(self) -> List[Message]:
        return self.messages

    def getUsers(self) -> List[User]:
        return self.users

    def __repr__(self) -> str:
        return f"Grupo: {self.name} - Usuários: {self.users} - Mensagens: {self.messages}"

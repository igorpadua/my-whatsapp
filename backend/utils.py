from group import Group
from user import User
from message import Message
from typing import List
from pika import BlockingConnection, ConnectionParameters, PlainCredentials


def conversationGroup(channel, groups: List = [], users: List = []) -> None:
    groupName: str = input("Digite o nome do grupo: ")
    group: Group

    if not existGroup(groupName):
        group = Group(groupName)
        groups.append(group)
    else:
        for gr in groups:
            if gr.getName == groupName:
                group = gr
    while True:
        print("1. Adicionar um usuário")
        print("2. Começar a conversa")
        print("3. Sair")

        option: str = input("Digite a opção desejada: ")

        if option == "1":
            name: str = input("Digite o nome do usuário: ")

            for user in users:
                if user.name == name:
                    group.addUser(user)
                    break
        elif option == "2":
            usuario: str = input("Digite o seu nome: ")

            for us in users:
                if us.name == usuario:
                    while True:
                        if not envitMessage(us, group, channel):
                            break
        elif option == "3":
            break


def conversationUser(channel, groups: List = [], users: List = []) -> None:
    contact: str = input("Digite o nome do usuário que você quer começar a conversa: ")
    usuario: str = input("Digite o seu nome: ")

    for user1 in users:
        if user1.name == contact:
            for user2 in users:
                if user2.name == usuario:
                    group: Group

                    if not existGroup(contact + usuario) and not existGroup(
                        usuario + contact
                    ):
                        group = Group(contact + usuario)
                        group.addUser(user1)
                        group.addUser(user2)
                        groups.append(group)
                    else:
                        for gr in groups:
                            if (
                                gr.getName == contact + usuario
                                or gr.getName == usuario + contact
                            ):
                                group = gr

                    while True:
                        if not envitMessage(user2, group, channel):
                            break

                    break


def envitMessage(user: User, group: Group, channel) -> bool:
    channel.exchange_declare(exchange=group.name, exchange_type="fanout")
    messageStr: str = input("Digite a mensagem ou sair: ")

    if messageStr == "sair":
        return False

    message: Message = Message(messageStr, user)
    channel.basic_publish(exchange=group.name, routing_key="", body=message.__repr__())

    group.addMessage(message)
    return True


def on_message(channel, method_frame, header_frame, body):
    print(body)


def existGroup(groupName: str, groups: List = []) -> bool:
    for group in groups:
        if group.getName == groupName:
            return True
    return False

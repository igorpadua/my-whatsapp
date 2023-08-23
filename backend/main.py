import sys
from typing import List
from time import sleep
from pika import BlockingConnection, ConnectionParameters, PlainCredentials

from group import Group
from user import User
from message import Message
from utils import conversationGroup, conversationUser, on_message

users: List[User] = []
groups: List[Group] = []


def main() -> None:
    connection = BlockingConnection(ConnectionParameters("localhost"))
    channel = connection.channel()
    while True:
        menu(channel)


def menu(channel) -> None:
    print("1. Adicionar um novo usuário")
    print("2. Listar usuários")
    print("3. Começar uma conversa com um usuário")
    print("4. Começar uma conversa em grupo")
    print("5. Listar conversas")
    print("6. Receber mensagens")
    print("7. Sair")

    option: str = input("Digite a opção desejada: ")

    if option == "1":
        name: str = input("Digite o seu nome: ")
        user: User = User(name)
        users.append(user)

    elif option == "2":
        print("Lista de usuários")
        for user in users:
            print(user)

    elif option == "3":
        conversationUser(channel, groups, users)
    elif option == "4":
        conversationGroup(channel, groups, users)
    elif option == "5":
        print("Lista de conversas")
        for group in groups:
            print(group)
    elif option == "6":
        nameGroup: str = input("Digite o nome do grupo: ")
        connection = BlockingConnection(ConnectionParameters("localhost"))

        channel = connection.channel()
        channel.exchange_declare(exchange=nameGroup, exchange_type="fanout")
        queue = channel.queue_declare(queue="", exclusive=True)
        channel.queue_bind(exchange=nameGroup, queue=queue.method.queue)
        channel.basic_consume(
            queue=queue.method.queue, on_message_callback=on_message, auto_ack=True
        )
        channel.start_consuming()

    elif option == "7":
        print("Saindo...")
        sleep(1)
        exit()


if __name__ == "__main__":
    main()
    pass

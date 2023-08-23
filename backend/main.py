from typing import List
from time import sleep

from group import Group
from user import User
from message import Message

users: List[User] = []
groups: List[Group] = []


def main() -> None:
    while True:
        menu()


def menu() -> None:
    print("1. Adicionar um novo usuário")
    print("2. Listar usuários")
    print("3. Começar uma conversa com um usuário")
    print("4. Começar uma conversa em grupo")
    print("5. Listar conversas")
    print("6. Sair")

    option: str = input("Digite a opção desejada: ")

    if option == '1':
        name: str = input("Digite o seu nome: ")
        user: User = User(name)
        users.append(user)

    elif option == '2':
        print("Lista de usuários")
        for user in users:
            print(user)

    elif option == '3':
        conversationUser()
    elif option == '4':
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

            if option == '1':
                name: str = input("Digite o nome do usuário: ")

                for user in users:
                    if user.name == name:
                        group.addUser(user)
                        break
            elif option == '2':
                usuario: str = input("Digite o seu nome: ")

                for us in users:
                    if us.name == usuario:

                        while True:
                            messageStr: str = input("Digite a mensagem ou sair: ")

                            if messageStr == 'sair':
                                break

                            message: Message = Message(messageStr, us)

                            group.addMessage(message)
                        break
            elif option == '3':
                break

    elif option == '5':
        print("Lista de conversas")
        for group in groups:
            print(group)
    elif option == '6':
        print("Saindo...")
        sleep(1)
        exit()

def conversationUser() -> None:
    contact: str = input("Digite o nome do usuário que você quer começar a conversa: ")
    usuario: str = input("Digite o seu nome: ")

    for user1 in users:
        if user1.name == contact:
            for user2 in users:
                if user2.name == usuario:
                    group: Group

                    if not existGroup(contact + usuario) and not existGroup(usuario + contact):
                        group = Group(contact + usuario)
                        group.addUser(user1)
                        group.addUser(user2)
                        groups.append(group)
                    else:
                        for gr in groups:
                            if gr.getName == contact + usuario or gr.getName == usuario + contact:
                                group = gr

                        while True:
                            messageStr: str = input("Digite a mensagem ou sair: ")

                            if messageStr == 'sair':
                                break

                            message: Message = Message(messageStr, user2)

                            group.addMessage(message)
                    break


def existGroup(groupName: str) -> bool:
    for group in groups:
        if group.getName == groupName:
            return True
    return False


if __name__ == "__main__":
    main()
    pass

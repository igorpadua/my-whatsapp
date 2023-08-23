from typing import List
from time import sleep

from group import Group
from user import User

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

    option: int = int(input("Digite a opção desejada: "))

    if option == 1:
        name: str = input("Digite o seu nome: ")
        user: User = User(name)
        users.append(user)

    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 6:
        print("Saindo...")
        sleep(1)
        exit()


if __name__ == "__main__":
    main()
    pass

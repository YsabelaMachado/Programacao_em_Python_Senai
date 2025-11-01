numero = int(input("Digite um número:"))

match numero:
    case numero if numero % 2 == 0:
        print("É Número par!")
    case _:
        print("É número impar!")    
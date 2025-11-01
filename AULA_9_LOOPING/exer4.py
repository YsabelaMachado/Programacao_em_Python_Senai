numero = int(input("Digite um número:"))

match numero:
    case numero if numero > 10:
        print("O número é maior que 10")
    case numero if numero < 10:
        print("O número é menor que 10")
    case _:
        print("O número é igual a 10")
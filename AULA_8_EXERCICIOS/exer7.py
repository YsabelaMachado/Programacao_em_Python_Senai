# Verifique se um número é divisível por 3 ou 5.
numero = int(input("Digite um número:"))

if numero % 3 == 0 or numero % 5 == 0:
    print("Esse número é divisível por 3 ou 5")
else:
    print("Esse número não é divisível por 3 ou 5")
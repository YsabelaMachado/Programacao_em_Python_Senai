# Determine se um número é múltiplo de 5 e 7.

numero = int(input("Digite um número:"))

if numero % 5 == 0 and numero % 7 == 0:
    print("Esse número é múltiplo de 5 e 7!")
else:
    print("Esse número não é múltiplo de 5 e 7!")
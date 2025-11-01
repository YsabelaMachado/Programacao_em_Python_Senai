# Verifique se um número é positivo e maior que 10
numero = int(input("Digite um número:"))

if numero > 0 and numero > 10:
    print("O número é positivo e maior que 10!")
elif numero > 0 and numero <10:
    print("O número é positivo mas não é maior que 10")
else:
    print("O número não é positivo e nem maior que 10!")
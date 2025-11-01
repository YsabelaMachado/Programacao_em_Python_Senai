var = 10
listas = [10,20,30,40]
tuplas = (10,30,5,30)
conjunto = {10,2,3,6}
dicionarios = {"key":"value"}

#nome = dado - str 10 5. True (dados primitivos)

#estruturas de fluxo de controle 
#if condição


#brasil
#carteira de motorista e ter 18 anos

idade = int(input("Digite sua idade:"))

carteira = input("Possui carteira?")

#condicional composta:
if idade >= 18:
    print("Pode dirigir")
else: #else nao tem condição
    print("Não pode dirigir")

#condicional composta - elif 
if idade >= 18:
    print("Maior de idade")
elif idade >= 18 and carteira == "sim":
    print("Pode dirigir")
else: #else não tem condição
    print("Menor e não pode dirigir")
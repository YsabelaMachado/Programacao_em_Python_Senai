# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Você pode votar!")
else:
    print("Você não pode votar!")
import random 

numero = random.randrange(1,50)
escolha = int(input("Escolha um número de 1 a 50:"))

if numero == escolha:
    print("Você ganhou o jogo!👌😊❤️")
else:
    print("Errou feio!🤦‍♀️🤷‍♂️🤡")
    print("O número aleatório é:", numero)

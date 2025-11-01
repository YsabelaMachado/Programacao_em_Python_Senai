import random

ppt_maquina = ['🪨','🧻','✂️']
ppt_jogador = ['🪨','🧻','✂️']

aleatorio = random.choice(ppt_maquina)
escolha = int(input('''
0 - 🪨
1 - 🧻
2 - ✂️
'''))

if aleatorio == ppt_jogador[escolha]:
    print("EMPATE")
    print("A maquina escolheu:", aleatorio)
    print("Você escolheu", ppt_jogador[escolha])

elif aleatorio == '🧻' and ppt_jogador[escolha] == '🪨':
    print("O computador ganhou")
    print("A maquina escolheu:", aleatorio)
    print("Você escolheu", ppt_jogador[escolha])

elif aleatorio == '🪨' and ppt_jogador[escolha] == '✂️':
    print("O computador ganhou")
    print("A maquina escolheu:", aleatorio)
    print("Você escolheu", ppt_jogador[escolha])

elif aleatorio == '✂️' and ppt_jogador[escolha] == '🧻':
    print("O computador ganhou")
    print("A maquina escolheu:", aleatorio)
    print("Você escolheu", ppt_jogador[escolha])

elif ppt_jogador[escolha] == '🧻' and aleatorio == '🪨':
    print("Você ganhou")
    print("A maquina escolheu:", aleatorio)
    print("Você escolheu", ppt_jogador[escolha])

elif ppt_jogador[escolha] == '🪨' and aleatorio == '✂️':
    print("Você ganhou")
    print("A maquina escolheu:", aleatorio)
    print("Você escolheu", ppt_jogador[escolha])

elif ppt_jogador[escolha] == '✂️' and aleatorio == '🧻':
    print("Você ganhou")
    print("A maquina escolheu:", aleatorio)
    print("Você escolheu", ppt_jogador[escolha])



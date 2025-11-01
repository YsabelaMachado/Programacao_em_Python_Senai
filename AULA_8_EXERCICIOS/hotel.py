banco_dados =  {}

nome1 = input("Nome:")
idade1 = input("Idade:")
senha1 = int(input("Senha:"))

nome2 = input("Nome:")
idade2 = input("Idade:")
senha2 = int(input("Senha:"))

nome3 = input("Nome:")
idade3 = input("Idade:")
senha3 = int(input("Senha:"))

banco_dados["nomes"] = [nome1, nome2, nome3]
banco_dados["idades"] = [idade1, idade2, idade3]
banco_dados["senhas"] = [senha1, senha2, senha3]

login_nome = input("Digite seu nome: ")
senha_acesso = int(input("Digite sua senha: "))


if login_nome in banco_dados["nomes"]:
    indice = banco_dados["nomes"].index(login_nome)
    if senha_acesso == banco_dados["senhas"][indice]:
        print("Seja bem-vindo ao Sistema!!!")

        print("Escolha o quarto:", nome1)
        quartos = ["Simples", "Duplo", "Luxo"]
        valor = ["100", "150", "250"]
        escolha  =  int(input("Escolha o quarto: id 0 = Simples | id 1 = Duplo | id 2 = Luxo:")) 
        quantidade  =  int(input("Qual a quantidade de dias de estadia:"))
        valor_final = quantidade * int(valor[escolha])
        print("Você escolheu o quarto:", quartos[escolha],"E quantidade de dias:", quantidade)
        print("O valor total é:", valor_final)

        print("Escolha o quarto:", nome2)
        quartos = ["Simples", "Duplo", "Luxo"]
        valor = ["100", "150", "250"]
        escolha  =  int(input("Escolha o quarto: id 0 = Simples | id 1 = Duplo | id 2 = Luxo:")) 
        quantidade  =  int(input("Qual a quantidade de dias de estadia:"))
        valor_final = quantidade * int(valor[escolha])
        print("Você escolheu o quarto:", quartos[escolha],"E quantidade de dias:", quantidade)
        print("O valor total é:", valor_final)

        print("Escolha o quarto:", nome3)
        quartos = ["Simples", "Duplo", "Luxo"]
        valor = ["100", "150", "250"]
        escolha  =  int(input("Escolha o quarto: id 0 = Simples | id 1 = Duplo | id 2 = Luxo:")) 
        quantidade  =  int(input("Qual a quantidade de dias de estadia:"))
        valor_final = quantidade * int(valor[escolha])
        print("Você escolheu o quarto:", quartos[escolha],"E quantidade de dias:", quantidade)
        print("O valor total é:", valor_final)
    else:
        print("Acesso negado, tente novamente!")

#logica
#variaveis

#tipos de dados primitivos 

#dado texto = "texto" string str()
#dado real = 5.0 float float()
#dado boleano = True bool bool()
#dado inteiro = 2 int int()

#print()

#variaveis = 20

#sinais aritmeticos 
# + - / // % **0.5
#saida é sempre um numero 
#n1 = 10
#n2 = 20
#print(n1 + n2)
#print(n1 - n2)
#print(n1 * n2)
#print(n1 / n2)
#apenas o primeiro decimal 
#print(n1 // n2)
#resto
#print(n1 % n2)
# # resto da conta de divisão 
# print(10  %   2 )


#sinais logicos
#saida é sempre True ou False
# n1 = 10
# n2 = 2
# print(n1 > n2)#maior
# print(n1 < n2)#menor
# print(n1 >= n2)#maior ou igual
# print(n1 <= n2)#menor ou igual
# print(n1 != n2)#diferente de 
# print(n1 == n2)#igual


# print("objeto") #output -- saida

# nome = input("Digite seu nome:") #input -- entrada
# #o input naturalmente gera um texto
# print("Seu nome é:", nome)

# n1 = float(input("Digite um numero:"))
# n2 = float(input("Digite um numero:"))
# soma = n1 + n2
# print("A soma é:", soma)

# n1 = float(input("Digite um numero:"))
# n2 = float(input("Digite um numero:"))
# subtracao = n1 - n2
# print("A subtração é:", subtracao)

# n1 = float(input("Digite um numero:"))
# n2 = float(input("Digite um numero:"))
# multiplicacao = n1 * n2
# print("A multiplicação é:", multiplicacao)

# n1 = float(input("Digite um numero:"))
# n2 = float(input("Digite um numero:"))
# divisao = n1 / n2
# print("A divisão é:", divisao)

#concatenação -- juntar dados

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
endereco = input("Digite seu endereço:")
curso = input("Digite seu curso:")
salario = float(input("Digite seu salario:"))

#concatenar
print("Nome:", nome)
print("Nome"+" "+nome)
print("Nome{}" .format(nome))
print(f"Nome{nome}")
print("Nome %s"%(nome))
print("Idade:", idade)
print("Endereço:", endereco)
print("Curso:", curso)
print("Salário:", salario)

#pular linha
#print 
#f''' ajjaaka {}'''
#\n
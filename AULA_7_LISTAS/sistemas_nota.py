lista_alunos = []
nome1 = input("Digite o nome do aluno:")
nome2 = input("Digite o nome do aluno:")
nome3 = input("Digite o nome do aluno:")

lista_alunos.append(nome1)
lista_alunos.append(nome2)
lista_alunos.append(nome3)

lista_alunos.extend([nome1,nome2, nome3])

notas_aluno1 = [float(input(f"Digite a nota 1 do aluno {nome1}:")),float(input(f"Digite a nota 2 do aluno {nome1}:"))]
notas_aluno2 = [float(input(f"Digite a nota 1 do aluno {nome2}:")),float(input(f"Digite a nota 2 do aluno {nome2}:"))]
notas_aluno3 = [float(input(f"Digite a nota 1 do aluno {nome3}:")),float(input(f"Digite a nota 2 do aluno {nome3}:"))]


media_aluno1 = sum(notas_aluno1)/len(notas_aluno1)
media_aluno2 = sum(notas_aluno2)/len(notas_aluno2)
media_aluno3 = sum(notas_aluno3)/len(notas_aluno3)

print("Media dos alunos:")

print(f'''
Médias:
Aluno {nome1} - {media_aluno1}
Aluno {nome2} - {media_aluno2}
Aluno {nome3} - {media_aluno3}
''')

aprovado1 = media_aluno1 >= 7
aprovado2 = media_aluno2 >= 7
aprovado3 = media_aluno3 >= 7

print(f'''
{nome1} APROVADO - {aprovado1} 
{nome2} APROVADO - {aprovado2}
{nome3} APROVADO - {aprovado3}
''')

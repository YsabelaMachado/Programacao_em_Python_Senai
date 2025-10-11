
#lista_vazia[0] = 100

#print(lista_vazia)

lista_ = [1,2,3]
lista_[0] = 100
# print(lista_)

#funções
#nomeDaFunção(lista)

#alteram
#funções para atribuir valores para a lista 

lista_.append(10)
print(lista_)

lista_.insert(1,200)
# print(lista_)

lista_.extend([10,20,30,40,50])
# print(lista_)

lista_+=([10,20,30,40,50,60])
# print(lista_)

#remover os dados 
lista_.pop()
# print(lista_)

lista_.pop(5)#remove o indice 
# print(lista_)

lista_.remove(200)#remove o numero
# print(lista_)

del lista_[0]
# print(lista_)

#tamanho
print(len(lista_))

#menor numero
print(min(lista_))

#maior numero
print(max(lista_))

#quanto tem um dado
print(lista_.count(10))

#ordenar a lista
lista_.sort()
print(lista_)

# reverter a sequencia da lista 
lista_.sort(reverse = True)
print(lista_)

#copiar a lista 
x  =  lista_.copy()
print(x)


#limpar a lista 
lista_.clear()
print(lista_)

l = list(range(1,200, 10))
print(l)


#métodos
#nome.nomeMédoto

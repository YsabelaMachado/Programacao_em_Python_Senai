# Verificando se uma string é vazia ou nãvar 
var = input("Digite algo: ")

match var:
    case "":          
        print("A string está vazia")
    case _:          
        print("A string não está vazia")



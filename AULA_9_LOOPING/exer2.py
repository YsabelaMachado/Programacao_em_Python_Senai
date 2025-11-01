n  =  int(input('Digite um numero: '))


match n:
    case 0:
        print('Zero')
    case n if n > 0:
        print('positivo')
    case n if n < 0:
        print('Negativo')
    case _:
        print('Desconhecido') 
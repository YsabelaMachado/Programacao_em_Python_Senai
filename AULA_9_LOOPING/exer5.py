idade = int(input("Digite a idade: "))

match idade:
    case idade if idade >= 65:
        print('idoso')
    case idade if idade >= 35 and idade <=64:
        print('Adulto')   
    case idade if idade >= 18 and idade <=34:
        print('jovem')  
    case idade if idade >= 14 and idade <=17:
        print('Adolescente')                   
    case _:
        print('Criança') 
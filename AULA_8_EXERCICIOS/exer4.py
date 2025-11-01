# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

lado1 = int(input("Digite o número do lado1: "))
lado2 = int(input("Digite o número do lado2: "))
lado3 = int(input("Digite o número do lado3: "))

if lado1 == lado2 == lado3:
    print("Isso é um triângulo equilátero!")
elif lado1 != lado2 != lado3:
    print("Isso é um triângulo escaleno!")
else:
    print("Isso é triângulo isósceles! ")
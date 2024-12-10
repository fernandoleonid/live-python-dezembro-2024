numero = int(input("Digite um número para a tabuada: "))
limite = int(input("Digite o limite máximo da tabuada: "))
contador = int(input("Digite o inicio da tabuada: "))
while contador <= limite:
    resultado = contador * numero
    print (f"{contador} x {numero} = {resultado}")
    contador += 1
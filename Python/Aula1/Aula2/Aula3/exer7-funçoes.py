# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.1

def soma_tres(um, dois, três):
    return um + dois + três
  
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

resultado = soma_tres(num1, num2, num3)

print(f"A soma dos três é: {resultado} ")

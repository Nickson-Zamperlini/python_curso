# Faça um programa que calcule o IMC e a situação de cada valor do IMC

# imc = peso / altura ** 2

# Abaixo de 18.5 - Abaixo do peso
# Entre 18.6 e 24.9 - Peso Ideal
# Entre 25.0 e 29.9 - Acima do Peso
# Entre 30.0 e 34.9 - Obesidade Grau I
# Entre 35.5 e 39.9 - Obesidade Grau II
# Acima de 40 - Obesidade Grau III

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / altura ** 2 

print(f"Seu IMC é: {imc:.2f}")

if imc <= 18.5:
    print("Abaixo do Peso")

elif imc <= 24.9:
    print("Peso ideal")

elif imc <= 29.9:
    print("Acima do Peso")

elif imc <= 34.9:    
    print("Obesidade Grau I")

elif imc <= 39.9:
    print("Obesidade Grau II")


else:
    print("Obesidade Grau III")

# Faça um Programa que receba 10 números inteiros e armazene-os em uma lista. Armazene os números
#  pares na lista pares e os números ímpares na lista ímpares. Imprima as três listas.

numeros = []
pares = []
impares = []

for i in range(1,11):
    num = int(input(f"Digite o {i}° número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Numeros: {numeros} \nPares: {pares} \nImpares: {impares}")
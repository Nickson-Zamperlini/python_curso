# Faça um programa que receba 5 números, armazene-os em uma lista e depois exiba a lista


numeros = []
for i in range(5):
    numero = float(input(f"Digite {i+1}º números : "))
    numeros.append(numero)
print("\nOs números em forma de lista: ")
print(numeros)
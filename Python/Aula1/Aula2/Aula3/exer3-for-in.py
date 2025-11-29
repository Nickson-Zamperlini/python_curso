# Crie um Programa que receba 5 números, armazene-os em uma lista depois, mostre a soma, a multiplicação e lista dos números.

numeros = []
soma = 0
mult = 1

for i in range(1,6):
    num = int(input(f"Digite o {i}° número: "))
    numeros.append(num)
    soma += num
    mult *= num

print(f"Números digitados: {numeros} \nSoma: {soma} \nMultiplicação: {mult}")
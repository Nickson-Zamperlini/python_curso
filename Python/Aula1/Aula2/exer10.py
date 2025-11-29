# faça um programa que receba 4 notas, armazene as notas em uma lista depois mostre as notas e a média na tela.

notas = []
soma = 0
media = 0

for i in range(1,5):
    nota = int(input(f"Digite a {i}° nota: "))
    soma += nota
    notas.append(nota)
    media = soma / len(notas)

print(f"As notas foram: {notas} \nE a média foi {media}")
# crie um programa que receba 10 números, armanezene-os em uma lista e mostre-os na ordem inversa.

lista_num = []

for i in range(1,11):
    num = int(input(f"Digite o {i}° número: "))
    lista_num.append(num)

lista_num.reverse()
print(lista_num)
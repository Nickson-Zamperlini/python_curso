# Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).

numero_inteiro = int(input("Digite um número inteiro: "))

if numero_inteiro % 2 == 0:
    print(f"O número {numero_inteiro} é PAR")

else: 
    print(f"O número {numero_inteiro} é IMPAR ")


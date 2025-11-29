# Crie um programa que funcione como uma calculadora, o programa deve ter um menu de opções para realizar os cálculos de adição, subtração, multiplicação e divisão,
#  o programa deve receber 2 números e realizar o cálculo conforme a opção que o usuário selecionar.

#def calculadora(escolha, n1, n2):
    #if escolha == 1: 
       # return n1 * n2 
    #if escolha == 2: 
      #  return n1 - n2 
   # if escolha == 3: 
      #  return n1 / n2
    #if escolha == 4: 
       # return n1 + n2 


#print("Calculadora")
#print("Digite 1 para multiplicar")
#print("Digite 2 para subtrair")
#print("Digite 3 para dividir")
#print("Digite 4 para somar")

#escolha = int(input("Escolha uma opção de calculo: "))
#n1 = int(input("Por favor escolha um número: "))
#n2 = int(input("Por favor escolha outro número: "))

#resultado = calculadora(escolha, n1, n2)
#print("Resultado", resultado)


#CORRIGIDO++

def menu():
    print("""
Selecione uma opção para realizar um calculo:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Sair
""")
    
def soma(n1, n2):
    print(f"\nA soma entre {n1} e {n2} é {n1+n2}")

def sub(n1, n2):
    print(f"\nA subtração entre {n1} e {n2} é {n1-n2}")

def multi(n1, n2):
    print(f"\nA multiplicação entre {n1} e {n2} é {n1*n2}")

def div(n1, n2):
    if n2 == 0:
        print("\nNão é possivel dividir um número por 0!")
    else:
        print(f"\nA soma entre {n1} e {n2} é {n1/n2}")

operacoes = {
    1: soma,
    2: sub,
    3: multi,
    4: div
}

while True:
    menu()

    op = int(input("Qual calculo deseja realizar? "))

    if op == 5:
        print("\nVocê escolheu sair!")
        break
    
    if op not in operacoes:
        print("\nOpção inválida!")
        continue

    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("\nDigite o segundo número: "))

    operacoes[op](n1, n2)
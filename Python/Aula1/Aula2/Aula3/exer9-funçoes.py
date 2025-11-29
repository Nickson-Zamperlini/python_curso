# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
 
def contadigitos(num:int):
    return len(str(num))

num = int(input("Digite um número inteiro: "))
print(f"Esse número digitado contém {contadigitos} digitos.")
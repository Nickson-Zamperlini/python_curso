# Crie um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
#  se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.



def verificacao_numeros(numero):

    if numero > 0:
        print(f"\nO seu argumento é positivo: {numero}")
        return "P"  
    elif numero < 0:
        print(f"\nO seu argumento é negativo: {numero}")
        return "N"  
    else:
        print(f"\nO seu argumento é zero: {numero}")
        return "N"
    
n = int(input("Digite um número: "))


resultado = verificacao_numeros(n)
print(f"O resultado é: {resultado}")


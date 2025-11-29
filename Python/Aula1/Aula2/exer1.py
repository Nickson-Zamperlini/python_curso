# Crie um programa que peça para o usuário digitar as 4 notas de um aluno e calcule a sua média, 
#se a média for maior que 7 o aluno está aprovado, se a média for menor que 2 o aluno está reprovado caso contrário o aluno está de recuperação.

nota1 = int(input("Digite uma nota: "))
nota2 = int(input("Digite uma segunda nota: "))
nota3 = int(input("Digite uma terceira nota: "))
nota4 = int(input("Digite uma quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A media do Aluno é igual a: {media} ")

if media >= 7:
    print("O aluno esta aprovado! ")
elif media <= 2:
    print("O aluno esta reprovado! ")
else: 
    print("O aluno esta de recuperação! ")
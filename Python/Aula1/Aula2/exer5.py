#crie um programa que peça para o usuário digitar o número para ver a sua tabuada utilizando while 

numero = int(input("Digite um número para ver a tabuada dele: "))

cont = 1 

while cont <= 10:
 
 print(f"{cont} x {numero} = {cont * numero}")

 cont += 1    

#crie um programa que peça para o usuário digitar um número para ver a sua tabuada utilizando for 

numero = int(input("Digite um número para ver a tabuada dele: "))

for i in range(0,11):
  
 print(f"{numero} x {i} = {i}")

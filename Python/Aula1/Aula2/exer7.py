#crie um programa que peça uma nota, entre zero a dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.




while True: 
    nota = int(input("Digite uma Nota de Zero a Dez: "))
 
    if nota <= 10 and nota >= 0:
        print("Valor Válido")
        break 
    else: 
        print("O valor é inválido")
  
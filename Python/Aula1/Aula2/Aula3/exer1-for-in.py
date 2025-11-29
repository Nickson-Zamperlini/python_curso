# Crie um programa que receba 10 letras separadas e armazene as vogais em uma lista e as 
# consoantes em outra. Ao final, exiba as duas listas e informe quantas vogais e quantas consoantes foram recebidas.

vogais = []
consoantes = []

for i in range(1,11):
    letra = input(f"Digite a {i}° letra: ")
    if letra.isalpha():
        if letra in "aeiou":
            vogais.append(letra)
        else:
            consoantes.append(letra)
    else:
        print("Você não digitou uma letra!")

print(f"Você digitou {len(vogais)} vogais - {vogais} \nVocê digitou {len(consoantes)} consoantes - {consoantes}")
# #Crie uma programa que funcione como um estoque, o programa deve permitir 
# # que o usuario liste os itens do estoque, adicione novos itens e remova itens

# print("""
# MENU: 
# 1. Listar 
# 2. Remover
# 3. Adicionar
# 4. Sair            
# """)       

# arquivo = open("estoque.txt", "r", encoding="utf-8")
   
   
# def listar():
    
 
         
#         with open("estoque.txt", "r") as arquivo:

# itens_estoque = arquivo.readlines()

# if len(itens_estoque) == 0:
#         print("Estoque vazio!")

# else: 
#         print("Itens no Estoque")

#         for item in itens_estoque: 
#             print("-", item.strip())


        
# def Adicionar():

#         item = input("Digite um item para ser adicionado a lista!").strip()

# with open("estoque.txt", "a") as arquivo:
#         arquivo.write (item + "\n")
#     print("Item adicionado!")


# def remover():
 
#         with open("estoque.txt", "r") as arquivo:
#             Item_remover = input("Digite qual item você deseja remover! ")  
#         itens_estoque = arquivo.readlines()
#         print("O item foi removido!")



print(
    """
Menu:
1. Listar
2. Remover
3. Adicionar
4. Sair
"""
)

opcao = input("Escolha uma opção: ")

if opcao == "1":
    with open("estoque.txt", "r", encoding="utf-8") as arquivo:
        itens = arquivo.readlines()

        if itens:
            for linha in itens:
                print(linha.strip())
        else:
            print("O arquivo está vazio!")

elif opcao == "2":
    nome = input("Digite o nome do produto que deseja remover: ")

    with open("estoque.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        novo_estoque = []

        for linha in linhas:
            if linha.strip() != nome:
                novo_estoque.append(linha)

        with open("estoque.txt", "w", encoding="utf-8") as arquivo:
            for item in novo_estoque:
                arquivo.write(item)

        print("Item removido!")

elif opcao == "3":
    item = input("Digite o nome do item que deseja adicionar: ")

    with open("estoque.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n {item}")

    print("Item adicionado com sucesso!")
    
elif opcao == "4":
    print("Você escolheu sair!")

else:
    print("Opção Inválida!")
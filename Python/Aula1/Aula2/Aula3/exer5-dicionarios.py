# Crie um dicionário que armazene informações das configurações de um computador, depois utilize a estrutura for para exibir as informações do computador.

computador = {
    "marca:": "acer", 
    "processador: ": "intel core i7", 
    "memoria: ": "8GB de memoria RAM", 
    "placa de video: ": "RTX-3050", 
    "tela: ": "15.6 Polegadas"
              
}
for chave, valor in computador.items():
    print(f"{chave}: {valor}")


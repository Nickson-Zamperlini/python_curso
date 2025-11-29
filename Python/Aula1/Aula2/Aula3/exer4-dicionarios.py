# Crie um dicionário com informações sobre um livro como ano, autor e gênero, acesse e imprima cada valor usando a chave.

livro = {
    "ano": 1954,
    "autor": "J.R.R Tolkien",
    "genero": "Fantasia",
    "nome": "O Senhor dos Aneis: A sociedade do Anel"
}

print(f"""
Informações sobre o livro:
Ano: {livro['ano']}
Autor: {livro['autor']}
Gênero: {livro['genero']}
Nome: {livro['nome']}
""")
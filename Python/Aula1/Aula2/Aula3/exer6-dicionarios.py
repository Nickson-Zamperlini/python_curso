# Crie um dicionário que armazene informações sobre vários alunos.
#  Cada aluno deve ter seu próprio dicionário contendo informações como idade, notas e curso. Depois, escreva um código para exibir essas informações.

turma = {
    "aluno1": {
        "nome" : "Nickson",
        "idade": 22,
        "curso": "ADS",
        "notas": [7,9,8,5]
    },

    "aluno2": {
        "nome" : "Lucas",
        "idade": 25,
        "curso": "EDS",
        "notas": [5,6,8,7]
    },

    "aluno3": {
        "nome" : "Luiz",
         "idade": 28,
        "curso": "CDC",
        "notas": [8,5,7,8]

    },

        "aluno4": {
        "nome" : "João",
        "idade": 20,
        "curso": "DevFullStack",
        "notas": [10,8,9,6]

    }
}

for chave, valor in turma.items():
    print(f"\n{chave}  \n{valor["nome"]}  \n{valor["idade"]}  \n{valor["curso"]}  \n{valor["notas"]}")
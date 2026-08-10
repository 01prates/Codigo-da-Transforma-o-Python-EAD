# Criando o dicionário do aluno
aluno = {
    "nome": "Maria Silva",
    "idade": 20,
    "notas": [8.5, 9.0, 7.5]
}

# Calculando a média das notas para enriquecer o programa
media = sum(aluno["notas"]) / len(aluno["notas"])

# Exibindo os valores
print("=== DADOS DO ALUNO ===")
print(f"Nome:  {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")
print(f"Média: {media:.2f}")
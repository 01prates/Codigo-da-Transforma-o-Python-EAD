import sqlite3

conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    status TEXT
)
""")
conexao.commit()

cursor.execute("INSERT INTO Tarefas (descricao, status) VALUES ('Estudar Python', 'Pendente')")
cursor.execute("INSERT INTO Tarefas (descricao, status) VALUES ('Fazer o desafio', 'Em andamento')")
conexao.commit()

cursor.execute("SELECT * FROM Tarefas")
print("Todas as Tarefas:", cursor.fetchall())

cursor.execute("UPDATE Tarefas SET status = 'Concluído' WHERE id = 1")
conexao.commit()

cursor.execute("DELETE FROM Tarefas WHERE id = 2")
conexao.commit()

cursor.execute("SELECT * FROM Tarefas")
print("Tarefas atualizadas:", cursor.fetchall())

conexao.close()
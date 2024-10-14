import sqlite3

# Conectando ao banco
conn = sqlite3.connect('system_marco.db')
cursor = conn.cursor()

# Criando uma tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
    
)
""")
print("conectado ao banco")

conn.commit()


import sqlite3

def criar_banco():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    sobrenome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL)''')
    conexao.commit()
    conexao.close()

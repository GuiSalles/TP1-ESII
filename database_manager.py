import sqlite3

DB_PATH = "usuarios.db"

def criar_tabela(DB_NAME = DB_PATH):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS avaliacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                sexo TEXT,
                peso REAL,
                altura REAL,
                imc REAL,
                classificacao TEXT,
                data TEXT
            )
        """)
        conn.commit()

def inserir_avaliacao(dados,DB_NAME = DB_PATH):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO avaliacoes (nome, idade, sexo, peso, altura, imc, classificacao, data)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            dados["nome"],
            dados["idade"],
            dados["sexo"],
            dados["peso"],
            dados["altura"],
            dados["imc"],
            dados["classificacao"],
            dados["data"]
        ))
        conn.commit()

def buscar_historico(nome, DB_NAME = DB_PATH):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT data, idade, sexo, peso, altura, imc, classificacao
            FROM avaliacoes
            WHERE nome = ?
            ORDER BY datetime(data) DESC
        """, (nome,))
    return cursor.fetchall()

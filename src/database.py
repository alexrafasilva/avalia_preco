import sqlite3
from datetime import datetime

def criar_tabela():
    """Cria a tabela de preços se não existir"""
    conn = sqlite3.connect('database/precos.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS precos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        preco REAL NOT NULL,
        data_coleta TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def inserir_preco(marca: str, modelo: str, preco: float):
    """Insere um novo preço na tabela"""
    conn = sqlite3.connect('database/precos.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO precos (marca, modelo, preco, data_coleta)
    VALUES (?, ?, ?, ?)
    ''', (marca, modelo, preco, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()

def obter_preco_medio() -> float:
    """Retorna o preço médio do mercado"""
    conn = sqlite3.connect('database/precos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(preco) FROM precos')
    preco_medio = cursor.fetchone()[0] or 100000  # Valor padrão se não houver dados
    conn.close()
    return preco_medio
import tempfile
import os
import sqlite3
from database_manager import criar_tabela, inserir_avaliacao, buscar_historico
import pytest

@pytest.fixture
def banco_teste(tmp_path):
   
    db_path = tmp_path / "test.db"
    criar_tabela(db_path)
    yield str(db_path)


def test_create_table(banco_teste):
    with sqlite3.connect(banco_teste) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='avaliacoes'")
        result = cursor.fetchone()
    assert result is not None

def test_inserir_avaliacao(banco_teste):
    dados = {
        "nome": "Ana",
        "idade": 30,
        "sexo": "Feminino",
        "peso": 65.0,
        "altura": 1.65,
        "imc": round(65.0 / (1.65 ** 2), 2),
        "classificacao": "Normal",
        "data": '2025-06-10'
    }

    inserir_avaliacao(dados, banco_teste)

    with sqlite3.connect(banco_teste) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM avaliacoes WHERE nome = 'Ana'")
        result = cursor.fetchone()

    assert result is not None

def test_buscar_historico(banco_teste):
    for peso in [70.0, 65.0, 60.0]:
        dados = {
            "nome": "nome_teste",
            "idade": 30,
            "sexo": "Feminino",
            "peso": peso,
            "altura": 1.65,
            "imc": round(peso / (1.65 ** 2), 2),
            "classificacao": "Normal",
            "data": '2025-06-10'
        }
        inserir_avaliacao(dados, banco_teste)

    resultado = buscar_historico("nome_teste", banco_teste)

    assert len(resultado) == 3

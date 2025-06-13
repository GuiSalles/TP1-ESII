import pytest
from imc_utils import calcular_imc, classificar_imc


def test_calculo_basico():
    assert calcular_imc(70, 1.75) == 22.86

def test_imc_arredondamento():
    assert calcular_imc(63, 1.70) == 21.8

def test_valores_minimos_validos():
    assert calcular_imc(30, 0.5) == 120.0
    

def test_classificacao_abaixo_do_peso():
    assert classificar_imc(17.0) == "Abaixo do peso"

def test_classificacao_limite_abaixo_do_peso():
    assert classificar_imc(18.49) == "Abaixo do peso"

def test_classificacao_peso_normal():
    assert classificar_imc(22.8) == "Peso normal"

def test_classificacao_limite_peso_normal():
    assert classificar_imc(24.9) == "Peso normal"

def test_classificacao_sobrepeso():
    assert classificar_imc(27.0) == "Sobrepeso"

def test_classificacao_limite_sobrepeso():
    assert classificar_imc(29.9) == "Sobrepeso"

def test_classificacao_obesidade_I():
    assert classificar_imc(33.0) == "Obesidade grau I"

def test_classificacao_obesidade_II():
    assert classificar_imc(38.0) == "Obesidade grau II"

def test_classificacao_obesidade_III():
    assert classificar_imc(42.0) == "Obesidade grau III"


def test_erro_altura_zero():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_erro_peso_negativo():
    with pytest.raises(ValueError):
        calcular_imc(-10, 1.70)
        
def test_erro_tipo_invalido():
    with pytest.raises(TypeError):
        calcular_imc("setenta", 1.75)

from unittest import result

from src.main import *
from unittest.mock import patch

def test_root():
    result = root()
    yield result
    assert result == {"message": "API Calculadora"}

def test_somar():
    # utilizei de exemplo os num 2 e 3, assim o resultado tem que ser obrigatoriamente 5.
    result = somar(2, 3)
    yield result
    assert result == {"Operação": "soma", "a": 2, "b": 3, "resultado": 5}

def test_subtrair ():
    # utilizei de exemplo os num 10 e 4, assim o resultado tem que ser obrigatoriamente 6.
    result = subtrair(10, 4)
    yield result
    assert result == {"Operação": "subtracao", "a": 10, "b": 4, "resultado": 6}

def test_multiplicar ():
    # utilizei de exemplo os num 3 e 3, assim o resultado tem que ser obrigatoriamente 9.
    result = multiplicar(3, 3)
    yield result
    assert result == {"Operação": "multiplicacao", "a": 3, "b": 3, "resultado": 9}

# dividi o teste de divisão em dois, sendo um de sucesso e outro de erro
def test_dividir():
    # utilizei de exemplo os num 10 e 2, assim o resultado tem que ser obrigatoriamente 5.
    result = dividir(10, 2)
    yield result
    assert result == {"Operação": "divisao", "a": 10, "b": 2, "resultado": 5.0}

    # utilizei de exemplo os num 10 e 0, assim o resultado tem que ser obrigatoriamente erro, considerando que não existe divisão por zero.
def test_dividir_por_zero():
    result = dividir(10, 0)
    yield result
    assert result == {"erro": "Não existe divisão por 0 (zero)"}

def test_numero_aleatorio():
    with patch("random.randint", return_value=123456):
        result = numero_aleatorio()
        yield result
        assert result == {"teste": True, "numero_aleatorio": 123456}

# dividi também a porcentagem em dois, sendo um de sucesso e outro de erro
def test_porcentagem():
    # utilizei de exemplo os num 50 e 10, assim o resultado tem que ser obrigatoriamente 5.
    result = porcentagem(50, 10)
    yield result
    assert result == {"Operação": "percentual", "a": 50, "b": 10, "resultado": 5.0}

    # utilizei de exemplo os num -5 e 10, assim o resultado tem que ser obrigatoriamente erro, considerando que os valores devem ser positivos.
def test_porcentagem_erro():
    result = porcentagem(-5, 10)
    yield result
    assert result == {"erro": "Os valores devem ser positivos"}

# dividi também a potenciação em dois, sendo um de sucesso e outro elevado a zero(em que o resultado é sempre 1).
def test_potenciacao():
    # utilizei de exemplo os num 2 e 3, assim o resultado tem que ser obrigatoriamente 8.
    result = potenciacao(2, 3)
    yield result
    assert result == {"Operação": "potência", "a": 2, "b": 3, "resultado": 8}

def test_potenciacao_elevado_a_zero():
    # utilizei de exemplo o b=0, assim o resultado tem que ser obrigatoriamente 1.
    result = potenciacao(5, 0)
    yield result
    assert result == {"Operação": "potência", "a": 5, "b": 0, "resultado": 1}


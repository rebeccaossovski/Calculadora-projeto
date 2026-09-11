from src.main import *
from unittest.mock import patch

def test_root():
   assert root() == {"message": "API Calculadora"}

def test_somar():
    # utilizei de exemplo os num 2 e 3, assim o resultado tem que ser obrigatoriamente 5.
    assert somar(2, 3) == {"Operação": "soma", "a": 2, "b": 3, "resultado": 5}

def test_subtrair ():
    # utilizei de exemplo os num 10 e 4, assim o resultado tem que ser obrigatoriamente 6.
    assert subtrair(10, 4) == {"Operação": "subtracao", "a": 10, "b": 4, "resultado": 6}

def test_multiplicar ():
    # utilizei de exemplo os num 3 e 3, assim o resultado tem que ser obrigatoriamente 9.
    assert multiplicar(3, 3) == {"Operação": "multiplicacao", "a": 3, "b": 3, "resultado": 9}

# dividi o teste de divisão em dois, sendo um de sucesso e outro de erro
def test_dividir():
    # utilizei de exemplo os num 10 e 2, assim o resultado tem que ser obrigatoriamente 5.
    assert dividir(10, 2) == {"Operação": "divisao", "a": 10, "b": 2, "resultado": 5.0}

    # utilizei de exemplo os num 10 e 0, assim o resultado tem que ser obrigatoriamente erro, considerando que não existe divisão por zero.
def test_dividir_por_zero():
    assert dividir(10, 0) == {"erro": "Não existe divisão por 0 (zero)"}

def test_numero_aleatorio():
    with patch("random.randint", return_value=12345):
        result = numero_aleatorio()

    assert result == {"teste": True, "numero_aleatorio": 12345}

# dividi também a porcentagem em dois, sendo um de sucesso e outro de erro
def test_porcentagem():
    # utilizei de exemplo os num 50 e 10, assim o resultado tem que ser obrigatoriamente 5.
    assert porcentagem(50, 10) == {"Operação": "percentual", "a": 50, "b": 10, "resultado": 5.0}

    # utilizei de exemplo os num -5 e 10, assim o resultado tem que ser obrigatoriamente erro, considerando que os valores devem ser positivos.
def test_porcentagem_erro():
    assert porcentagem(-5, 10) == {"erro": "Os valores devem ser positivos"}

# dividi também a potenciação em dois, sendo um de sucesso e outro elevado a zero(em que o resultado é sempre 1).
def test_potenciacao():
    # utilizei de exemplo os num 2 e 3, assim o resultado tem que ser obrigatoriamente 8.
    assert potenciacao(2, 3) == {"Operação": "potência", "a": 2, "b": 3, "resultado": 8}

def test_potenciacao_elevado_a_zero():
    # utilizei de exemplo o b=0, assim o resultado tem que ser obrigatoriamente 1.
    assert potenciacao(5, 0) == {"Operação": "potência", "a": 5, "b": 0, "resultado": 1}



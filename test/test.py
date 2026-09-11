from src.main import *
from unittest.mock import patch
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "API Calculadora"}

@pytest.mark.asyncio
async def test_somar():
    # utilizei de exemplo os num 2 e 3, assim o resultado tem que ser obrigatoriamente 5.
    result = await somar(2, 3)
    assert result == {"Operação": "soma", "a": 2, "b": 3, "resultado": 5}

@pytest.mark.asyncio
async def test_subtrair():
    # utilizei de exemplo os num 10 e 4, assim o resultado tem que ser obrigatoriamente 6.
    result = await subtrair(10, 4)
    assert result == {"Operação": "subtracao", "a": 10, "b": 4, "resultado": 6}

@pytest.mark.asyncio
async def test_multiplicar():
    # utilizei de exemplo os num 3 e 3, assim o resultado tem que ser obrigatoriamente 9.
    result = await multiplicar(3, 3)
    assert result == {"Operação": "multiplicacao", "a": 3, "b": 3, "resultado": 9}

# dividi o teste de divisão em dois, sendo um de sucesso e outro de erro
@pytest.mark.asyncio
async def test_dividir():
    # utilizei de exemplo os num 10 e 2, assim o resultado tem que ser obrigatoriamente 5.
    result = await dividir(10, 2)
    assert result == {"Operação": "divisao", "a": 10, "b": 2, "resultado": 5.0}

@pytest.mark.asyncio
async def test_dividir_por_zero():
    # utilizei de exemplo os num 10 e 0, assim o resultado tem que ser obrigatoriamente erro, considerando que não existe divisão por zero.
    result = await dividir(10, 0)
    assert result == {"erro": "Não existe divisão por 0 (zero)"}

@pytest.mark.asyncio
async def test_numero_aleatorio():
    with patch("random.randint", return_value=12345):
        result = await numero_aleatorio()
        assert result == {"teste": True, "numero_aleatorio": 12345}

# dividi também a porcentagem em dois, sendo um de sucesso e outro de erro
@pytest.mark.asyncio
async def test_porcentagem():
    # utilizei de exemplo os num 50 e 10, assim o resultado tem que ser obrigatoriamente 5.
    result = await porcentagem(50, 10)
    assert result == {"Operação": "percentual", "a": 50, "b": 10, "resultado": 5.0}

@pytest.mark.asyncio
async def test_porcentagem_erro():
    # utilizei de exemplo os num -5 e 10, assim o resultado tem que ser obrigatoriamente erro, considerando que os valores devem ser positivos.
    result = await porcentagem(-5, 10)
    assert result == {"erro": "Os valores devem ser positivos"}

# dividi também a potenciação em dois, sendo um de sucesso e outro elevado a zero(em que o resultado é sempre 1).
@pytest.mark.asyncio
async def test_potenciacao():
    # utilizei de exemplo os num 2 e 3, assim o resultado tem que ser obrigatoriamente 8.
    result = await potenciacao(2, 3)
    assert result == {"Operação": "potência", "a": 2, "b": 3, "resultado": 8}

@pytest.mark.asyncio
async def test_potenciacao_elevado_a_zero():
    # utilizei de exemplo o b=0, assim o resultado tem que ser obrigatoriamente 1.
    result = await potenciacao(5, 0)
    assert result == {"Operação": "potência", "a": 5, "b": 0, "resultado": 1}
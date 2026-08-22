from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Calculadora"}

@app.get("/somar/{a}/{b}")
async def somar(a: int, b: int):
    resultado = a + b
    return {"Operação": "soma", "a":a, "b":b, "resultado":resultado}

@app.get("/subtrair/{a}/{b}")
async def subtrair (a: int, b: int):
    resultado = a - b
    return {"Operação": "subtracao", "a":a, "b":b, "resultado":resultado}

@app.get("/multiplicar/{a}/{b}")
async def multiplicar (a: int, b: int):
    resultado = a * b
    return {"Operação": "multiplicacao", "a":a, "b":b, "resultado":resultado}

@app.get("/dividir/{a}/{b}")
async def dividir (a: int, b: int):
    if b == 0:
        return {"erro": "Não existe divisão por 0 (zero)"}
    resultado = a / b
    return {"Operação": "divisao", "a":a, "b":b, "resultado":resultado}

@app.get("/aleatorio")
async def numero_aleatorio():
    import random
    return {"numero_aleatorio": random.randint(1, 100)}

@app.get("/porcentagem/{a}/{b}")
async def porcentagem(a: float, b: float):
    resultado = (a * b) / 100
    return {"Operação": "percentual", "a": a, "b": b, "resultado": resultado}
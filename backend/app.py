from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

matriz = [
    [1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1]
]

def reflexiva(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] != 1:
            return "Falso"
    return "Verdadeiro"

def simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return "Falso"
    return "Verdadeiro"

def antisimetrica(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            if matriz[i][j] == 1 and matriz[j][i] == 1:
                return "Falso"
    return "Verdadeiro"

def assimetrica(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            if matriz[i][j] == matriz[j][i] and matriz[i][j] == 1:
                return "Falso"
    return not simetrica(matriz)

def transitiva(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            for k in range(len(matriz)):
                if matriz[i][j] == 1 and matriz[j][k] == 1 and matriz[i][k] != 1:
                    return "Falso"
    return "Verdadeiro"

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"]
)


@app.get('/get_data')
async def get_data():
    valorReflexivo = reflexiva(matriz)
    valorSimetrico = simetrica(matriz)
    valorAntissimetrico = antisimetrica(matriz)
    valorAssimetrico = assimetrica(matriz)
    valorTransitivo = transitiva(matriz)

    return {
        'reflexiva': valorReflexivo,
        'simetrica': valorSimetrico,
        'antissimetrica': valorAntissimetrico,
        'assimetrica': valorAssimetrico,
        'transitiva': valorTransitivo
        }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777)
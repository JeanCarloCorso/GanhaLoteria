import random

def GeraBilhete():
    bilhete = [[0 for _ in range(10)] for _ in range(6)]
    contador = 0
    for x in range(6):
        for j in range(10):
            contador += 1
            bilhete[x][j] = '{:02d}'.format(contador)
    return bilhete

def MostraBilhete(bilhete):
    print("+---------------------------------------+")
    print("+------Representação-dos-Quadrantes-----+", end="")
    for x in range(6):
        if (x) % 2 == 0:
            print("\n+-------+-------+-------+-------+-------+")
        else:
            print("")
        print("| ", end="")
        for j in range(10):
            fim = ""
            if j % 2 != 0:
                fim = " | "
            elif j != 9:
                fim = " "
            print(bilhete[x][j], end=fim)
    print("\n+-------+-------+-------+-------+-------+")

def EscolheNumeros():
    intervaloQuadrantes = range(1, 16)
    quadrantesSelecionados = set()

    linhas = []
    colunas = []

    while len(quadrantesSelecionados) < 6:
        quadrantesSelecionados.add(random.choice(intervaloQuadrantes))
    quadrantesSelecionados = list(quadrantesSelecionados)

    for x in range(7):
        linhas.append(random.choice([0, 1]))
        colunas.append(random.choice([0, 1]))
    
    bilhete = GeraBilhete()
    ImprimeJogos(bilhete, quadrantesSelecionados, linhas, colunas)

def ImprimeJogos(bilhete, quadrantes, linhas, colunas):
    numerosSorteados = []
    for x in range(len(quadrantes)):
        delta = quadrantes[x] // 5
        linha = (linhas[x] * 2) + linhas[x]
        coluna = (quadrantes[x] - (delta * 5)) * 2 + colunas[x]
        numerosSorteados.append(bilhete[linha][coluna])

    print(numerosSorteados)


#MostraBilhete(bilhete)
EscolheNumeros()
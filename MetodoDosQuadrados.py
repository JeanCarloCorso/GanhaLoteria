import random

def GeraBilhete():
    bilhete = [[0 for _ in range(10)] for _ in range(6)]
    contador = 0
    for x in range(6):
        for j in range(10):
            contador += 1
            bilhete[x][j] = '{:02d}'.format(contador)
    return bilhete

def EscolheNumeros():
    intervaloQuadrantes = range(15)
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
        linha = (delta * 2) + linhas[x]
        coluna = (quadrantes[x] - (delta * 5)) * 2 + colunas[x]
        numerosSorteados.append(bilhete[linha][coluna])

    MostraBilhete(bilhete, numerosSorteados)

def MostraBilhete(bilhete, numerosSorteados):
    print("+-------------------------------+")
    print("+----Representação-do-Bilhete---+")
    print("+-------------------------------+")
    
    for x in range(6):
        if (x) != 0:
            print("|")
        print("| ", end="")
        for j in range(10):
            fim = " "
            if bilhete[x][j] in numerosSorteados:
                print("\033[1;30;107m" + str(bilhete[x][j]) + "\033[0m", end=fim)
            else:
                print(bilhete[x][j], end=fim)
    print("|\n+-------------------------------+")
#MostraBilhete(bilhete)
EscolheNumeros()
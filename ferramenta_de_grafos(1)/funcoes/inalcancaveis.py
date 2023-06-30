from classes.grafo import Grafo
from funcoes.alcancaveis import Alcancaveis


def Inalcancaveis(grafos: list[Grafo], verticeInicial):
    vInalcancaveis = []

    alcancaveis = Alcancaveis(grafos, verticeInicial)

    for i in range(len(alcancaveis)):
        if alcancaveis[i]:
            inalcancaveis = set(grafos[i].vertices) - alcancaveis[i]
            vInalcancaveis.append(inalcancaveis)
    
    return vInalcancaveis
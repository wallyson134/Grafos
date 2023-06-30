from classes.grafo import Grafo
from funcoes.ha_vertices_alcancaveis import haVerticesAlcancaveis


def haVerticesInalcancaveis(grafos: list[Grafo], verticeInicial):
    haVerticesInalcancaveis = []

    alcancaveis = haVerticesAlcancaveis(grafos, verticeInicial)

    for i in range(len(alcancaveis)):
        if alcancaveis[i]:
            inalcancaveis = set(grafos[i].vertices) - alcancaveis[i]
            haVerticesInalcancaveis.append(inalcancaveis)
    
    return haVerticesInalcancaveis
from classes.grafo import Grafo
from collections import deque

def Alcancaveis(grafos: list[Grafo], verticeInicial):
    haVerticesAlcancaveis = []

    for grafo in grafos:
        vertices = grafo.vertices
        arestas = grafo.arestas

        if verticeInicial in vertices:
            
            alcancaveis = set()
            
            
            queue = deque()
            
            
            queue.append(verticeInicial)
            alcancaveis.add(verticeInicial)
            
            while queue:
                current_vertex = queue.popleft()
                
            
                neighbors = [edge[1] for edge in arestas if edge[0] == current_vertex]
                for neighbor in neighbors:
                    if neighbor not in alcancaveis:
                        queue.append(neighbor)
                        alcancaveis.add(neighbor)
            
            haVerticesAlcancaveis.append(alcancaveis)

    return haVerticesAlcancaveis
        

        

        
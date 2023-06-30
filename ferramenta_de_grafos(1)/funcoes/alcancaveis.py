from classes.grafo import Grafo
from collections import deque

def haVerticesAlcancaveis(grafos: list[Grafo], verticeInicial):
    haVerticesAlcancaveis = []

    for grafo in grafos:
        vertices = grafo.vertices
        arestas = grafo.arestas

        if verticeInicial in vertices:
            # Criar um conjunto para armazenar os vértices alcançáveis
            alcancaveis = set()
            
            # Criar uma fila para armazenar os vértices a serem visitados
            queue = deque()
            
            # Iniciar a busca em largura a partir do vértice de início
            queue.append(verticeInicial)
            alcancaveis.add(verticeInicial)
            
            while queue:
                current_vertex = queue.popleft()
                
                # Encontrar os vizinhos do vértice atual
                neighbors = [edge[1] for edge in arestas if edge[0] == current_vertex]
                
                # Adicionar os vizinhos não visitados à fila e ao conjunto de alcançáveis
                for neighbor in neighbors:
                    if neighbor not in alcancaveis:
                        queue.append(neighbor)
                        alcancaveis.add(neighbor)
            
            haVerticesAlcancaveis.append(alcancaveis)

    return haVerticesAlcancaveis
        

        

        
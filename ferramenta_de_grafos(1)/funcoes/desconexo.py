from classes.grafo import Grafo

def verificaConexao(vertices, arestas):
    if not vertices:
            return False
    
    verticesAlcancaveis = set()
    queue = [vertices[0]] 

    while queue:
        verticeAtual = queue.pop(0)
        verticesAlcancaveis.add(verticeAtual)

        for aresta in arestas:
            if aresta[0] == verticeAtual and aresta[1] not in verticesAlcancaveis:
                verticesAlcancaveis.add(aresta[1])
                queue.append(aresta[1])

            elif aresta[1] == verticeAtual and aresta[0] not in verticesAlcancaveis:
                verticesAlcancaveis.add(aresta[0])
                queue.append(aresta[0])

    return len(verticesAlcancaveis) == len(vertices)

def saoDesconexos(grafos: list[Grafo]):
    saoDesconexos = []

    for grafo in grafos:
        vertices = grafo.vertices
        arestas = grafo.arestas

        if not verificaConexao(vertices, arestas):
            saoDesconexos.append(grafo)
    
    return saoDesconexos
            



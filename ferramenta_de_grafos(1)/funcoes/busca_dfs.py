from classes.grafo import Grafo

def busca_Dfs(grafos: list[Grafo], partida, chegada):
    haCaminho: list[Grafo] = []
    
    for grafo in grafos:
        caminho = dfs2(grafo, partida, chegada)

        if caminho:
            haCaminho.append((grafo.id, caminho))
        else:
            haCaminho.append((grafo.id, "caminho não encontrado"))

    return haCaminho

def dfs2(grafo: Grafo, partida, chegada):
    vertices = grafo.vertices
    arestas = grafo.arestas

    pilha = [[partida]]
    visitado = set()

    while pilha:
        path = pilha.pop()
        verticeAtual = path[-1]

        if verticeAtual == chegada:
            return path
        
        if verticeAtual in visitado:
            continue

        visitado.add(verticeAtual)
        for aresta in arestas:
            if aresta[0] == verticeAtual and aresta[1] not in visitado:
                new_path = list(path)
                new_path.append(aresta[1])
                pilha.append(new_path)

            elif aresta[1] == verticeAtual and aresta[0] not in visitado:
                new_path = list(path)
                new_path.append(aresta[0])
                pilha.append(new_path)


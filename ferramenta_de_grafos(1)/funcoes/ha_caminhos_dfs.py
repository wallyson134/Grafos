from classes.grafo import Grafo

def haCaminhoDfs(grafos: list[Grafo], partida, chegada):
    haCaminho: list[Grafo] = []
    
    for grafo in grafos:
        caminho = dfs2(grafo, partida, chegada)

        if caminho:
            haCaminho.append((grafo.id, caminho))
        else:
            haCaminho.append((grafo.id, "caminho não encontrado"))

    return haCaminho

def dfs(grafo, start, end):
    # Verificar se os vértices de início e fim estão no grafo
    if start not in grafo.vertices or end not in grafo.vertices:
        return None

    # Criar um dicionário para rastrear os predecessores de cada vértice visitado
    predecessors = {}

    # Realizar a busca em profundidade
    _dfs_util(grafo, start, end, predecessors)

    # Construir o caminho a partir dos predecessores
    path = _construct_path(start, end, predecessors)

    return path

def _dfs_util(grafo, current_vertex, end, predecessors):
    # Verificar se chegamos ao vértice de destino
    if current_vertex == end:
        return True

    # Encontrar os vizinhos do vértice atual
    neighbors = [edge[1] for edge in grafo.arestas if edge[0] == current_vertex]

    # Explorar os vizinhos não visitados recursivamente
    for neighbor in neighbors:
        if neighbor not in predecessors:
            predecessors[neighbor] = current_vertex
            if _dfs_util(grafo, neighbor, end, predecessors):
                return True

    return False

def _construct_path(start, end, predecessors):
    # Construir o caminho a partir dos predecessores
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = predecessors.get(current_vertex)

    # Inverter o caminho para obter a ordem correta
    path.reverse()

    # Retornar o caminho encontrado
    return path

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


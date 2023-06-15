import json
from collections import deque


class GraphTool:
    def __init__(self):
        self.graphs = {}

    def load_graphs_from_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.graphs = data

    def is_multigraph(self):
        multigraphs = []
        for graph_id, graph in self.graphs.items():
            for vertex in graph:
                if len(graph[vertex]) > len(set(graph[vertex])):
                    multigraphs.append(graph_id)
                    break
        return multigraphs

    def is_pseudograph(self):
        pseudographs = []
        for graph_id, graph in self.graphs.items():
            for vertex in graph:
                if vertex in graph[vertex]:
                    pseudographs.append(graph_id)
                    break
        return pseudographs

    def is_disconnected(self):
        disconnected_graphs = []
        for graph_id, graph in self.graphs.items():
            visited = set()
            queue = deque([next(iter(graph))])

            while queue:
                vertex = queue.popleft()
                visited.add(vertex)
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

            if len(visited) != len(graph):
                disconnected_graphs.append(graph_id)

        return disconnected_graphs

    def is_complete(self):
        complete_graphs = []
        for graph_id, graph in self.graphs.items():
            vertices = set(graph.keys())
            is_complete = True
            for vertex in graph:
                if set(graph[vertex]) != vertices - {vertex}:
                    is_complete = False
                    break
            if is_complete:
                complete_graphs.append(graph_id)

        return complete_graphs

    def get_vertex_degrees(self, graph_id):
        graph = self.graphs.get(graph_id)
        if graph:
            degrees = {}
            for vertex in graph:
                degrees[vertex] = len(graph[vertex])
            return degrees
        return {}

    def get_vertex_degree(self, graph_id, vertex):
        graph = self.graphs.get(graph_id)
        if graph:
            return len(graph.get(vertex, []))
        return 0

    def find_reachable_vertices(self, graph_id, start_vertex):
        graph = self.graphs.get(graph_id)
        if graph:
            visited = set()
            queue = deque([start_vertex])

            while queue:
                vertex = queue.popleft()
                visited.add(vertex)
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

            return visited
        return set()

    def find_unreachable_vertices(self, graph_id, start_vertex):
        graph = self.graphs.get(graph_id)
        if graph:
            reachable_vertices = self.find_reachable_vertices(graph_id, start_vertex)
            all_vertices = set(graph.keys())
            return all_vertices - reachable_vertices
        return set()

    def bfs(self, graph_id, start_vertex, target_vertex):
        graph = self.graphs.get(graph_id)
        if graph:
            visited = set()
            queue = deque([(start_vertex, [])])

            while queue:
                vertex, path = queue.popleft()
                visited.add(vertex)
                path.append(vertex)

                if vertex == target_vertex:
                    return path

                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, path[:]))

        return []

    def dfs(self, graph_id, start_vertex, target_vertex):
        graph = self.graphs.get(graph_id)
        if graph:
            visited = set()
            stack = [(start_vertex, [])]

            while stack:
                vertex, path = stack.pop()
                visited.add(vertex)
                path.append(vertex)

                if vertex == target_vertex:
                    return path

                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        stack.append((neighbor, path[:]))

        return []
      
    def run_command(self, command):
        parts = command.split()

        if parts[0] == 'grafos':
            if parts[1] == 'carregar':
                try:
                    filename = parts[2]
                    self.load_graphs_from_json(filename)
                    print('Arquivo carregado com sucesso.')
                except IndexError:
                    print('Comando inválido. Uso correto: grafos carregar <filename>')
            elif parts[1] == 'multigrafos':
                multigraphs = self.is_multigraph()
                if multigraphs:
                    print('Os seguintes grafos são multigrafos:')
                    for graph_id in multigraphs:
                        print(graph_id)
                else:
                    print('Nenhum grafo é um multigrafo.')

            elif parts[1] == 'pseudografos':
                pseudographs = self.is_pseudograph()
                if pseudographs:
                    print('Os seguintes grafos são pseudografos:')
                    for graph_id in pseudographs:
                        print(graph_id)
                else:
                    print('Nenhum grafo é um pseudografo.')

            elif parts[1] == 'desconexos':
                disconnected_graphs = self.is_disconnected()
                if disconnected_graphs:
                    print('Os seguintes grafos são desconexos:')
                    for graph_id in disconnected_graphs:
                        print(graph_id)
                else:
                    print('Nenhum grafo é desconexo.')

            elif parts[1] == 'completos':
                complete_graphs = self.is_complete()
                if complete_graphs:
                    print('Os seguintes grafos são completos:')
                    for graph_id in complete_graphs:
                        print(graph_id)
                else:
                    print('Nenhum grafo é completo.')

            elif parts[1] == 'graus':
                graph_id = parts[2]
                if len(parts) == 3:
                    degrees = self.get_vertex_degrees(graph_id)
                    print(f'Graus dos vértices do grafo {graph_id}:')
                    for vertex, degree in degrees.items():
                        print(f'Vertice {vertex}: {degree} grau(s)')
                elif len(parts) == 5 and parts[3] == 'vertice':
                    vertex = parts[4]
                    degree = self.get_vertex_degree(graph_id, vertex)
                    print(f'Grau do vértice {vertex} do grafo {graph_id}: {degree}')

            elif parts[1] == 'alcancaveis':
                graph_id = parts[2]
                start_vertex = parts[3]
                reachable_vertices = self.find_reachable_vertices(graph_id, start_vertex)
                print(f'Vertices alcançáveis a partir do vértice {start_vertex} do grafo {graph_id}:')
                for vertex in reachable_vertices:
                    print(vertex)

            elif parts[1] == 'inalcancaveis':
                graph_id = parts[2]
                start_vertex = parts[3]
                unreachable_vertices = self.find_unreachable_vertices(graph_id, start_vertex)
                print(f'Vertices inalcançáveis a partir do vértice {start_vertex} do grafo {graph_id}:')
                for vertex in unreachable_vertices:
                    print(vertex)

            elif parts[1] == 'bfs':
                graph_id = parts[2]
                start_vertex = parts[3]
                target_vertex = parts[4]
                path = self.bfs(graph_id, start_vertex, target_vertex)
                if path:
                    print(f'Caminho encontrado do vértice {start_vertex} ao vértice {target_vertex}:')
                    print(' -> '.join(path))
                else:
                    print(f'Não foi possível encontrar um caminho do vértice {start_vertex} ao vértice {target_vertex}.')
            elif parts[1] == 'dfs':
                graph_id = parts[2]
                start_vertex = parts[3]
                target_vertex = parts[4]
                path = self.dfs(graph_id, start_vertex, target_vertex)
                if path:
                    print(f'Caminho encontrado do vértice {start_vertex} ao vértice {target_vertex}:')
                    print(' -> '.join(path))
                else:
                    print(f'Não foi possível encontrar um caminho do vértice {start_vertex} ao vértice {target_vertex}.')
            elif parts[1] == 'sair':
                exit()
            else:
                print('Comando inválido.')
        else:
            print('Comando inválido.')


    def start(self):
        print('Bem-vindo(a) à ferramenta de análise de grafos.')
        while True:
            command = input('> ')
            self.run_command(command)


tool = GraphTool()
tool.start()

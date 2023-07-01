class Grafo:
    def __init__(self, id, vertices, arestas):
        self.id = id
        self.vertices = vertices
        self.arestas = arestas
        self.criarMatrizDeAdjacencia()

    def criarMatrizDeAdjacencia(self):
        self.matrizADJ = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]

        for aresta in self.arestas:
            origem = self.vertices.index(aresta[0])
            destino = self.vertices.index(aresta[1])
            self.matrizADJ[origem][destino] = 1
            
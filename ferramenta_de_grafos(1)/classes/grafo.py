class Grafo:
    def __init__(self, id, vertices, arestas):
        self.id = id
        self.vertices: list = vertices
        self.arestas: list = arestas
        self.criarMatrizDeAdjacencia()

    def criarMatrizDeAdjacencia(self):
        self.matrizADJ = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]

        for aresta in self.arestas:
            origem = self.vertices.index(aresta[0])
            destino = self.vertices.index(aresta[1])
            # self.matrizADJ[origem][destino] = 1 
            self.matrizADJ[origem][destino] = 1 if self.matrizADJ[origem][destino] == 0 else self.matrizADJ[origem][destino]+1

            # self.matrizADJ[destino][origem] = 1 APENAS P/ GRAFO N DIRECIONADO


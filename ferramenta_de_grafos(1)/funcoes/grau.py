from classes.grafo import Grafo

def grauDeTodosOsVertices(grafo: Grafo):
    listaDeGraus = []
    for vertice in grafo.vertices:
        # listaDeGraus.append((vertice, grauDeVerticeEspecifico(grafo, vertice)))
        listaDeGraus.append(grauDeVerticeEspecifico(grafo, vertice))

    return listaDeGraus
    # print("Esse grafo tem os seguintes graus em cada vértice:")
    # for i in range(len(listaDeGraus)):
    #     print(grafo.vertices[i],"- grau: ",listaDeGraus[i])



def grauDeVerticeEspecifico(grafo: Grafo, vertice):
    grau = 0
    for i in range(len(grafo.arestas)):
        # if grafo.arestas[i][0] == vertice or grafo.arestas[i][1] == vertice:
        if vertice in grafo.arestas[i]: #msm coisa acima
            grau = grau + 1
    # print("o grau do vértice ",vertice," é ",grau)
    return grau

from classes.grafo import Grafo

def Multigrafos(grafos: list[Grafo]):
    Multigrafos: list[Grafo] = []

    for grafo in grafos:
        
        for i in range(len(grafo.matrizADJ)):
            for j in range(len(grafo.matrizADJ[i])):

                if (grafo.matrizADJ[i][j]>1):
                    Multigrafos.append(grafo)
                    break
        
    return Multigrafos
   
from classes.grafo import Grafo

def Multigrafos(grafos: list[Grafo]):
    saoMultigrafos: list[Grafo] = []

    for grafo in grafos:
        
        for i in range(len(grafo.matrizADJ)):
            for j in range(len(grafo.matrizADJ[i])):

                if (grafo.matrizADJ[i][j]>1):
                    saoMultigrafos.append(grafo)
                    break
        
    return saoMultigrafos
 
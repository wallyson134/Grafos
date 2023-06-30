from classes.grafo import Grafo

def Pseudografos(grafos: list[Grafo]):
    Pseudografos: list[Grafo] = []

    for grafo in grafos:

        for i in range(len(grafo.matrizADJ)):
            if (grafo.matrizADJ[i][i]>0):
                    Pseudografos.append(grafo)
                    break
        
    return Pseudografos
    

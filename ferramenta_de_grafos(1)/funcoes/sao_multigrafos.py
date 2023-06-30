from classes.grafo import Grafo

def saoMultigrafos(grafos: list[Grafo]):
    saoMultigrafos: list[Grafo] = []

    for grafo in grafos:
        
        for i in range(len(grafo.matrizADJ)):
            for j in range(len(grafo.matrizADJ[i])):

                if (grafo.matrizADJ[i][j]>1):
                    saoMultigrafos.append(grafo)
                    break
        
    return saoMultigrafos
    # print("dentre esses grafos, são multigrafos os com os seguintes IDs:") 
    # for grafo in saoMultigrafos:
    #     print(grafo.id)
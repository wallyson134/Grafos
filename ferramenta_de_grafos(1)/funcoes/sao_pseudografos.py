from classes.grafo import Grafo

def saoPseudografos(grafos: list[Grafo]):
    saoPseudografos: list[Grafo] = []

    for grafo in grafos:

        for i in range(len(grafo.matrizADJ)):
            if (grafo.matrizADJ[i][i]>0):
                    saoPseudografos.append(grafo)
                    break
        
    return saoPseudografos
    # print("dentre esses grafos, são pseudgrafos os com os seguintes IDs:") 
    # for grafo in saoPseudografos:
    #     print(grafo.id)



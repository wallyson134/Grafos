import json
from classes.grafo import Grafo


def carregarGrafos(arquivo):
    try:
        file = open(arquivo)
        dados = json.load(file)
    except:
        raise Exception()
    else:
        grafos: list[Grafo] = []
        # aqui vou ter uma lista com todos os grafos em forma de objeto
        for i in dados['graphs']:
            grafos.append(
                Grafo(
                    i['id'],
                    i['vertices'],
                    i['edges'],
                )
            )

        print("carregado", len(grafos), "grafos")
        return grafos
    # return 

    

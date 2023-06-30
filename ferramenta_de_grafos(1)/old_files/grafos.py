import json
from classes.grafo import Grafo

from funcoes.sao_multigrafos import saoMultigrafos
from funcoes.sao_pseudografos import saoPseudografos
from funcoes.grau import grauDeVerticeEspecifico
from funcoes.grau import grauDeTodosOsVertices
from funcoes.sao_completos import sao_completos
from funcoes.ha_caminhos_bfs import ha_caminhos_bfs
from funcoes.ha_caminhos_dfs import ha_caminhos_dfs

# TODO: colocar pra ler de um arquivo passado por parametro no terminal
file = open('c:/Users/franr/Documents/uespi/periodo 7/teoria dos grafos/atividades-teoria-dos-grafos/graphs.json')
dados = json.load(file)

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

# for i in range(len(grafos)):
#     print(grafos[i].vertices)

# testando multigrafos
# multigrafos = saoMultigrafos(grafos)
# for i in range(len(multigrafos)):
#     print(multigrafos[i].id)

# testando grau de vértice especifico
# pseudografos = saoPseudografos(grafos)
# for i in range(len(multigrafos)):
#     print(multigrafos[i].id)

# testando grau de todos os vértices
# print(grauDeTodosOsVertices(grafos[0]))

# testando se sao completos
# completos = sao_completos(grafos)
# for completo in completos:
#    print(completo.id)

# testando bfs
# caminhos = ha_caminhos_bfs(grafos, "A", "B")
# for caminho in caminhos:
#     print("id: ",caminho[0], ", caminho: ", caminho[1])

# testando dfs
#TODO: DANDO ERRO NO GRAFO 7, CORRIGIR
# caminhos = ha_caminhos_dfs(grafos, "A", "B")
# for caminho in caminhos:
#     print("id: ",caminho[0], ", caminho: ", caminho[1])
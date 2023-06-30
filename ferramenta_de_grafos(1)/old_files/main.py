import argparse
import json

from classes.grafo import Grafo

# Crie um objeto ArgumentParser
parser = argparse.ArgumentParser(description='Ferramenta de Grafos')

# Adicione os argumentos esperados
parser.add_argument('comando', help='Comando a ser executado')
parser.add_argument('arquivo', help='Arquivo de entrada')
parser.add_argument('--id', help='ID do vértice')
parser.add_argument('--vertice', help='Nome do vértice')

args = parser.parse_args()

if args.comando == 'carregar':
    # testa se foi passado nome do arquivo
    if not args.arquivo:
        print('O comando "carregar" requer um arquivo como argumento.')

    try:
        file = open(args.arquivo)
    except:
        print(f'ocorreu um erro ao tentar carregar "{args.arquivo}"')
    else:    
        print(f'Carregando arquivo: {args.arquivo}')
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

        print("feito! foram carregados", len(grafos), "grafos")

        


# elif args.comando == 'grau':
#     if args.id and args.vertice:
#         print(f'Cálculo do grau do vértice {args.vertice} com ID {args.id}')
#     else:
#         print('O comando "grau" requer os argumentos --id e --vertice.')

# Exemplo de uso:
# python grafos.py carregar --arquivo arquivo.json
# python grafos.py grau --id 1 --vertice A
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def adicionar_vertice(grafo, vertice):
    grafo.add_node(vertice)

def adicionar_aresta(grafo, vertice1, vertice2):
    grafo.add_edge(vertice1, vertice2)

def obter_tipo_grafo(grafo):
    num_vertices = len(grafo.nodes())
    num_arestas = len(grafo.edges())

    if num_vertices == 0:
        return "Grafo vazio"

    if num_arestas == 0:
        return "Grafo sem arestas"

    if num_arestas == num_vertices - 1:
        return "Grafo árvore"

    if num_arestas == num_vertices * (num_vertices - 1) / 2:
        return "Grafo completo"

    return "Grafo geral"

def visualizar_grafo(grafo):
    app = tk.Tk()
    app.title("Visualização do Grafo")

    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    pos = nx.spring_layout(grafo)
    nx.draw_networkx(grafo, pos=pos, ax=ax)
    ax.set_axis_off()

    tipo_grafo = obter_tipo_grafo(grafo)
    tipo_label = tk.Label(app, text="Tipo do grafo: " + tipo_grafo)
    tipo_label.pack()

    app.mainloop()

# Exemplo de uso
grafo = nx.Graph()
adicionar_vertice(grafo, 'A')
adicionar_vertice(grafo, 'B')
adicionar_vertice(grafo, 'C')
adicionar_aresta(grafo, 'A', 'B')
adicionar_aresta(grafo, 'B', 'C')
visualizar_grafo(grafo)

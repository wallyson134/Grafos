#import matplotlib.pyplot as plt
#import tkinter as tk
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#import tkinter as tk
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.tipo_grafo = ""
    
    def adicionar_vertice(self, vertice):
        self.vertices.append(vertice)
    
    def adicionar_aresta(self, vertice1, vertice2):
        self.arestas.append((vertice1, vertice2))
    
    def obter_tipo_grafo(self):
        num_vertices = len(self.vertices)
        num_arestas = len(self.arestas)
    
        if num_vertices == 0:
            return "Grafo vazio"
    
        if num_arestas == 0:
            return "Totalmente Desconexo"
        
        for i in range(num_arestas):
            vertice1, vertice2 = self.arestas[i]
            if vertice1 == vertice2:
                return "Pseudografo"
                
        if self.verificar_multigrafo():
            return "Multigrafo"
            
        return "Grafo genérico"
    
    def obter_grau_vertices(self):
        graus = {}
        for vertice in self.vertices:
            graus[vertice] = 0
    
        for aresta in self.arestas:
            vertice1, vertice2 = aresta
            graus[vertice1] += 1
            graus[vertice2] += 1
    
        return graus
    
    def verificar_multigrafo(self):
        for i in range(len(self.arestas)):
            for j in range(i + 1, len(self.arestas)):
                vertice1a, vertice2a = self.arestas[i]
                vertice1b, vertice2b = self.arestas[j]
                if (vertice1a == vertice1b and vertice2a == vertice2b) or (vertice1a == vertice2b and vertice2a == vertice1b):
                    return True
        return False
    
    

    """def visualizar_grafo():
        app = tk.Tk()
        app.title("Visualização do Grafo")

        fig, ax = plt.subplots(figsize=(6, 4))
        canvas = FigureCanvasTkAgg(fig, master=app)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        pos = {}
        y = 0
        for vertice in vertices:
            pos[vertice] = (vertices.index(vertice), y)
            y -= 0.1

        for aresta in arestas:
            vertice1, vertice2 = aresta
            x = [pos[vertice1][0], pos[vertice2][0]]
            y = [pos[vertice1][1], pos[vertice2][1]]
            ax.plot(x, y, '-o', color='black')

        for vertice, coord in pos.items():
            x, y = coord
            ax.text(x, y, vertice, ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

        ax.set_axis_off()

        tipo_grafo = obter_tipo_grafo()
        tipo_label = tk.Label(app, text="Tipo do grafo: " + tipo_grafo)
        tipo_label.pack()

        app.mainloop()
    """
# Exemplo de 
grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_aresta('A', 'B')
#grafo.adicionar_aresta('B', 'B')
#grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('C', 'A')
grafo.adicionar_aresta('B', 'C')
#visualizar_grafo()
grafo.tipo_grafo = grafo.obter_tipo_grafo()
grafo.graus = grafo.obter_grau_vertices()
for vertice, grau in grafo.graus.items():
    print("Grau do vértice", vertice, ":", grau)
    
print("O Grafo é um " + grafo.tipo_grafo)
from funcoes.carregar_grafos import carregarGrafos
from funcoes.multigrafos import Multigrafos
from funcoes.pseudografo import Pseudografos
from funcoes.grau_do_vertice import grauDeTodosOsVertices, grauDeVerticeEspecifico
from funcoes.completo import Completos
from funcoes.desconexo import Desconexos
from funcoes.alcancaveis import Alcancaveis
from funcoes.inalcancaveis import Inalcancaveis
from funcoes.busca_bfs import CaminhoBfs
from funcoes.busca_dfs import CaminhoDfs


print("GRAFOS \nEscolha um comando para analise do grafo")


class FerramentaGrafos:
    continuarPrograma = True
    grafos = []

    def Comandos(self, comando: str):
        if comando[0] == "grafos":
            if comando[1] == "sair":
                print("fim do programa!\n")
                self.continuarPrograma = False
            
            
            elif len(comando) == 3 and comando[1] == "carregar":
                try:
                    self.grafos = carregarGrafos(comando[2])
                except:
                    print("Arquivo não encontrado!")


            elif comando[1] == "multigrafos":
                if self.existemGrafos():
                    multigrafos = Multigrafos(self.grafos)
                    print("Os grafos multigrafos são os com os seguintes IDs:") 
                    for grafo in multigrafos:
                        print(grafo.id)
                else:
                    self.exibeMsgSemGrafosCarregados()

            

            elif comando[1] == "pseudografos":
                if self.existemGrafos():
                    pseudografos = Pseudografos(self.grafos)
                    print("Os pseudografos são os com o seguinte IDs:") 
                    for grafo in pseudografos:
                        print(grafo.id)
                else:
                    self.exibeMsgSemGrafosCarregados()
            

            elif comando[1] == "desconexos":
                if self.existemGrafos():
                    desconexos = Desconexos(self.grafos)
                    print("Os grafos desconexos são os de IDs::") 
                    for grafo in desconexos:
                        print(grafo.id)
                else:
                    self.exibeMsgSemGrafosCarregados()
            
            

            elif comando[1] == "completos":
                if self.existemGrafos():
                    completos = Completos(self.grafos)
                    print("Os grafos completos são os de IDs:") 
                    for grafo in completos:
                        print(grafo.id)
                else:
                    self.exibeMsgSemGrafosCarregados()


            elif len(comando) == 3 and comando[1] == "graus":
                if self.existemGrafos():
                    idGrafo = int(comando[2].split("=")[1])

                    listaDeGraus = grauDeTodosOsVertices(self.grafos[idGrafo-1])
                    print("graus em cada vértice:")
                    for i in range(len(listaDeGraus)):
                        print(self.grafos[idGrafo-1].vertices[i]," - ", listaDeGraus[i])
                else:
                    self.exibeMsgSemGrafosCarregados()
            

            elif len(comando) == 4 and comando[1] == "grau":
                if self.existemGrafos():
                    idGrafo = int(comando[2].split("=")[1])
                    verticeGrafo = comando[3].split("=")[1].strip("'").strip('"')

                    grau = grauDeVerticeEspecifico(self.grafos[idGrafo-1], verticeGrafo)
                    print("o grau do vértice ",verticeGrafo," desse grafo é ",grau)
                else:
                    self.exibeMsgSemGrafosCarregados()
            

            elif len(comando) == 3 and comando[1]=='alcancaveis':
                if self.existemGrafos():
                    verticeInicial = comando[2].split("=")[1].strip("'").strip('"')

                    alcancaveis = Alcancaveis(self.grafos, verticeInicial)
                    for i in range(len(alcancaveis)):
                        # a linha abaixo faz aparecer a msg 'nenhum' caso n haja vertices alcancaveis
                        verticesAlcancaveis = alcancaveis[i] if alcancaveis[i] else 'nenhum'
                        print("os vertices alcancaveis no grafo ",i+1," a partir de ",verticeInicial," são: ",verticesAlcancaveis,"\n")
                else:
                    self.exibeMsgSemGrafosCarregados()

            
            elif len(comando) == 3 and comando[1]=='inalcancaveis':
                if self.existemGrafos():
                    verticeInicial = comando[2].split("=")[1].strip("'").strip('"')

                    inalcancaveis = Inalcancaveis(self.grafos, verticeInicial)
                    for i in range(len(inalcancaveis)):
                        # a linha abaixo faz aparecer a msg 'nenhum' caso n haja vertices inalcancaveis
                        verticesInalcancaveis = inalcancaveis[i] if inalcancaveis[i] else 'nenhum'
                        print("os vertices inalcancaveis no grafo ",i+1," a partir de ",verticeInicial," são: ",verticesInalcancaveis,"\n")
                else:
                    self.exibeMsgSemGrafosCarregados()
            

            elif len(comando) == 4 and comando[1] == 'bfs':
                if self.existemGrafos():
                    partida = comando[2].split('=')[1].strip('"')
                    chegada = comando[3].split('=')[1].strip('"')

                    caminhoBfs = CaminhoBfs(self.grafos, partida, chegada)

                    print("BFS")
                    for caminho in caminhoBfs:
                        print("o caminho do vértice ",partida," até o vértice ",chegada," no grafo de ID ",caminho[0]," é ",caminho[1])
                
                else:
                    self.exibeMsgSemGrafosCarregados()


            elif len(comando) == 4 and comando[1] == 'dfs':
                if self.existemGrafos():
                    partida = comando[2].split('=')[1].strip('"')
                    chegada = comando[3].split('=')[1].strip('"')

                    caminhoDfs = CaminhoDfs(self.grafos, partida, chegada)

                    print("DFS")
                    for caminho in caminhoDfs:
                        print("o caminho do vértice ",partida," até o vértice ",chegada," no grafo de ID ",caminho[0]," é ",caminho[1])
                
                else:
                    self.exibeMsgSemGrafosCarregados()


            else:
                print("comando digitado incorretamente! tente novamente")
            
        else:
            print("comando digitado incorretamente! tente novamente")
    
    def existemGrafos(self):
        return True if self.grafos else False
    
    def exibeMsgSemGrafosCarregados(self):
        print("primeiro carregue um json com grafos!")


ferramentaGrafos = FerramentaGrafos()

while ferramentaGrafos.continuarPrograma:
    comando = str(input("\n> "))
    comandoAtual = comando.split()
    try:
        ferramentaGrafos.Comandos(comandoAtual)
    except:
        print("comando digitado incorretamente! tente novamente")




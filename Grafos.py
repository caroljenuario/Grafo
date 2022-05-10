#caroline jenuario
#alexandre cabral
import random
class Grafo:


    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adicionar_aresta(self, u, v):
        self.grafo[u-1][v-1] += 1    

    def imprimir(self):
        print('Matriz de adjacências:')
        for i in range(self.vertices):
            print(self.grafo[i])

v = int(input('Quantidade de vértices: \n'))
g = Grafo(v)

a = int(input('Quantidade de arestas: \n'))
for i in range(a): 
    valor = random.randrange(1,10)
    valor_2 = random.randrange(1,10)
    u = valor 
    v = valor_2
    g.adicionar_aresta(u, v)
   
g.imprimir()
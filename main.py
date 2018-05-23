from labyrinth import labyrinth
from methods import search

engine = search()





lab = labyrinth(4)
lab.generate()
graph = lab.getGraph()

# '1:1' -> '10:10'

graph.show()

# path = engine.gradient(graph, '1:1', '4:4' )
# path = engine.dfs(graph, '1:1', '4:4' )
# path = engine.equalCosts(graph, '1:1', '4:4' )
path = engine.bfs(graph, '1:1', '3:4' )
# path = engine.bfst(graph, '1:1', '4:4' )

def printPath(path):
    directions = {
        1: 'UP',
        2: 'RIGHT',
        3: 'DOWN',
        4: 'LEFT'
    }
    print('['+str.join(', ', map(lambda d: directions[d], path))+']')

# print(path1)
# print(path2)
# print(path3)
printPath(path)
lab.show()
from labyrinth import labyrinth
from methods import search

engine = search()





lab = labyrinth(4)
lab.generate()
graph = lab.getGraph()

# '1:1' -> '10:10'

graph.show()

path = engine.gradient(graph.getNodes(), '1:1', '4:4' )
path = engine.dfs(graph.getNodes(), '1:1', '4:4' )
path = engine.equalCosts(graph.getNodes(), '1:1', '4:4' )
path = engine.bfs(graph.getNodes(), '1:1', '4:4' )

print(path)
lab.show()
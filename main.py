#!/usr/bin/env python
from labyrinth import labyrinth
from methods import search

engine = search()

def printPath(path):
    directions = {
        1: 'UP',
        2: 'RIGHT',
        3: 'DOWN',
        4: 'LEFT'
    }
    print('['+str.join(', ', map(lambda d: directions[d], path))+']')



lab = labyrinth(4)
lab.generate()
graph = lab.getGraph()

# '1:1' -> '10:10'
lab.show()
graph.show()

path = None
while(True):
    print('\nКакой метод поиска вы хотите использовать?')
    print("1 - поиск по градиенту\n"+
            "2 - поиск по глубине\n"+
            "3 - поиск по равным ценам\n"+
            "4 - поиск по ширине\n"+
            "0 - Остановить"
        )
    num = input()
    num = int(num)
    if num >=1 and num <=4:
        lab.show()
    if num == 1:
        path = engine.gradient(graph, '1:1', '4:4' )
    elif num == 2 :
        path = engine.dfs(graph, '1:1', '4:4' )
    elif num == 3:
        path = engine.equalCosts(graph, '1:1', '4:4' )
    elif num == 4:
        path = engine.bfs(graph, '1:1', '4:4' ) 
    else:
        break
    if path is not None:
        printPath(path)

# path = engine.gradient(graph, '1:1', '4:4' )
# path = engine.dfs(graph, '1:1', '4:4' )
# path = engine.equalCosts(graph, '1:1', '4:4' )
# path = engine.bfs(graph, '1:1', '4:4' )
# path = engine.bfst(graph, '1:1', '4:4' )



# print(path1)
# print(path2)
# print(path3)



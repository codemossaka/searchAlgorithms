from random import randint

from graph import graph

class labyrinth:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    directions = {
        UP: [0, -1],
        RIGHT: [1, 0],
        DOWN: [0, 1],
        LEFT: [-1, 0]
    }
    def __init__(self, size):
        self.labyrinth = {}
        self.size = size

    def invertDirection(self, direction):
        return (direction + 1) % 4 + 1

    def _addEdge(self, x, y, direction):
        x2 = x + self.directions[direction][0]
        y2 = y + self.directions[direction][1]
        if (x2 < 1) or (x2 > self.size) or (y2 < 1) or (y2 > self.size):
            return False
        node1 = str(x) + ':' + str(y)
        node2 = str(x2) + ':' + str(y2)
        if node2 not in self.labyrinth:
            self.labyrinth[node2] = {}
        self.labyrinth[node1][direction] = True
        self.labyrinth[node2][self.invertDirection(direction)] = True
        return True

    def generate(self):

        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                directions = []
                node = str(x) + ':' + str(y)
                if node not in self.labyrinth:
                    self.labyrinth[node] = {}
                d = randint(1, 4)
                while not self._addEdge(x, y, d):
                    d = randint(1, 4)

                d2 = randint(1, 4)
                while (d2 != d) and (not self._addEdge(x, y, d2)):
                    d2 = randint(1, 4)

    def getGraph(self):
        g = graph()
        for node in self.labyrinth:
            for d in self.labyrinth[node]:
                (x, y) = node.split(':')
                subNode = str(int(x) + self.directions[d][0])+':'+str(int(y) + self.directions[d][1])
                g.addNode(subNode)
                g.addEdge(node, subNode, d)
                g.addEdge(subNode, node, self.invertDirection(d))
        return g

    def show(self):
        row = "#"
        for x in range(1, self.size + 2):
            row = row + "###"
        print(row)

        for y in range(1, self.size + 1):
            row = "#  "
            for x in range(1, self.size + 1):
                key = str(x) + ':' + str(y)
                c = "  "
                if (self.RIGHT in self.labyrinth[key]):
                    c = "--"
                row = row + "+" + c
            print(row + "#")

            if y >= self.size:
                break

            row = "#  "
            for x in range(1, self.size + 1):
                key = str(x) + ':' + str(y)
                c = "  "
                if (self.DOWN in self.labyrinth[key]):
                    c = "| "
                row = row + c + " "
            print(row + "#")

        row = "#"
        for x in range(1, self.size + 2):
            row = row + "###"
        print(row)





























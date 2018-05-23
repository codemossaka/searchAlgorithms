import collections

class search:

    def __init__(self):
        pass

    def dfs(self, graph, start, target, visited=None):
        if visited is None:  # проверяем пустоту посешенный ход
            visited = set()  # инициализируем неповторяемый массив посещаемых ходов
        if self.isTarget(start, target):
            print('Цель достигнута')
            return []
        else:
            print('Цель не достигнута')

        visited.add(start)  # добовляем вершину
        # print(start, end=" ")  # отображаем ее
        for move in graph.getMoves(start):  # цикл чтобы поторялось действие
            node = move['node']
            if node in visited:
                continue
            path = self.dfs(graph, node, target, visited)  # вызываем функцию опять (рекурсивная функцию)
            if path is not None:
                return [move['direction']] + path
        return None

    def isTarget(self,node, target):
        return node == target
        
    def bfs(self, graph, start, target):
        # Track the visited and unvisited nodes using queue
        seen, queue = set([start]), collections.deque([start])  #инициализируем
        path = {start: []}
        while queue:    #проходим пока перемение не пустое
            vertex = queue.popleft()    #убовляем с лево в перемение
            for move in graph.getMoves(vertex):
                node = move['node']
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
                    path[node] = path[vertex] + [move['direction']]
        return path[target]

    # def bfst(self, graph, start, target):

    #     def get_path(vertex):
    #         curr_vertex = vertex
    #         parents_data_list = collections.deque([vertex['node']])
    #         while curr_vertex.parent:
    #             curr_vertex = curr_vertex.parent
    #             parents_data_list.appendleft(curr_vertex['node'])
    #         print(list(parents_data_list))
    #         return list(parents_data_list)

    #     Vertex = collections.namedtuple('Vertex', ['node', 'parent'])

    #     queue = collections.deque([Vertex(start, None)])  # инициализируем

    #     while True:
    #         vertex = queue.popleft()  # убовляем с лево в перемение
    #         for move in graph.getMoves(vertex['node']):
    #             next_vertex = Vertex(move['node'], vertex)
    #             if next_vertex['node'] == target:
    #                 return get_path(next_vertex)
    #             queue.append(next_vertex)


    def equalCosts(self, graph, start, target):
        seen, queue = {start: 0}, collections.deque([start])  #seen - массив просмотренных вершин (ключ: наименование вершины, значение: наилучшая длина пути), queue - очередь смежных вершин
        path = {start: []} #path - массив для каждой вершины где содержится наилучший путь
        while queue:
            vertex = queue.popleft()    #извлекаем очередную вершину из очереди
            for move in graph.getMoves(vertex):
                pathLength = seen[vertex]+1 # длина пути в вершину node через вершину vertex
                node = move['node']
                if node not in seen: # добаляем вершину в очередь если она еще не была просмотрена
                    queue.append(node)
                if (node not in seen) or (pathLength < seen[node]): # если найденый путь короче уже записанного для вершины (или она еще не была посещена)
                    seen[node] = pathLength # добавляем вершину в список посещенных и записываем текущую длину пути
                    path[node] = path[vertex] + [move['direction']] # записываем путь на основе пути для вершины vertex
        return path[target]

    def gradient(self, graph, start, target):
        self.start = start
        self.target = target

        def getXY(node):
            (x, y) = node.split(':')
            return (int(x), int(y))

        def cost(node):
            (x, y) = getXY(node['node'])
            (targetX, targetY) = getXY(self.target)
            cost = max(abs(x-targetX), abs(y-targetY))
            print("cost[{0}, {1}] = {2}".format(x, y, cost))
            return cost


        def dfs(graph, node=None, visited=None):
            if visited is None:
                visited = set()
            if node is None:
                node = self.start
            if self.isTarget(node, self.target):
                print('Цель достигнута')
                return []
            else:
                print('Цель не достигнута')
            visited.add(node)

            for move in sorted(graph.getMoves(node), key=cost):
                if move['node'] in visited:
                    continue
                path = dfs(graph, move['node'], visited)
                if path is not None:
                    return [move['direction']] + path

            return None

        return dfs(graph)





# Более мощные алгоритмы поиска используют априорные
# знания человека – эксперта об особенностях решения задач в заданной предметной
# области. В эвристических программах эти знания реализуются с помощью оценочных
# функций. Оценочной функцией называется функция от n аргументов, представляющие
# собой некоторые числовые (или приведенные к числовым) параметры предметной
# области и вычисляющая меру близости любой из текущих ситуаций к целевой. Можно
# представить значения оценочной функции как точки N – мерного пространства.

# Алгоритм заключается в использовании правила
# максимизации с опорой на поиск в глубину. При этом, возможные ходы выбираются
# не случайным образом, а в соответствии со значениями оценочной функцией. То
# есть сначала выбирается наилучший ход, а потом другой, оцененный ранее как
# менее предпочтительный.


class graph:

    def __init__(self, nodes = None):
        if nodes is None:
            nodes = {}
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    # def removeNode(node):
    #	if node in self.nodes:
    #		del self.nodes[node]

    def addEdge(self, nodeFrom, nodeTo):
        if nodeFrom == nodeTo:
            raise Exception('Error addEdge: "nodeTo" must differ from "nodeFrom"')

        self.addNode(nodeFrom)
        self.addNode(nodeTo)

        # if nodeFrom not in self.nodes:
        #	raise Exception('Error addEdge: node '+nodeFrom+' not exist')
        # if nodeTo not in self.nodes:
        #	raise Exception('Error addEdge: node '+nodeTo+' not exist')

        if nodeTo not in self.nodes[nodeFrom]:
            self.nodes[nodeFrom].add(nodeTo) # [nodeTo] = True
        if nodeFrom not in self.nodes[nodeTo]:
            self.nodes[nodeTo].add(nodeFrom) # [nodeFrom] = True

    # def removeEdge(nodeFrom, nodeTo):

    def show(self):
        print("{")
        for node in self.nodes:
            subNodes = []
            for subNode in self.nodes[node]:
                subNodes.append(subNode)
            print(    "'"+node+"': ["+str.join(", ", (subNodes))+"]")
        print("}")
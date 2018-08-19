# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# class Solution:
#     def __init__(self):
#         self.nodedict = {}
#
#     def clone(self,node):
#         if not node:
#             return None
#         if node.label in self.nodedict:
#             return self.nodedict.get(node.label)
#         clonenode = UndirectedGraphNode(node.label)
#
#         self.nodedict[node.label] = clonenode
#
#         for neighboor in node.neighbors:
#             clonenode.neighbors.append(self.clone(neighboor))
#         return clonenode
#
#     def cloneGraph(self, node):
#         return self.clone(node)

class Solution:

    def cloneGraph(self, node):
        if not node:
            return None
        clonenode = UndirectedGraphNode(node.label)
        queue,nodedict = [],{}
        queue.append(node)
        nodedict[node.label] = clonenode

        while len(queue) != 0:
            cur = queue.pop()
            for neighbor in cur.neighbors:
                if not neighbor.label in nodedict:
                    queue.insert(0,neighbor)
                    nodedict[neighbor.label] = UndirectedGraphNode(neighbor.label)
                nodedict[cur.label].neighbors.append(nodedict.get(neighbor.label))
        return clonenode

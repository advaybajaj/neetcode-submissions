"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        d = dict() # hashmap of original to their copy

        def dfs(currNode):
            if not currNode:
                return None

            if currNode in d:
                return d[currNode]

            newNode = Node(currNode.val, [])
            d[currNode] = newNode

            for n in currNode.neighbors:
                newNode.neighbors.append(dfs(n))

            return newNode

        return dfs(node)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
    
        def getNeighbor(node):
            return node.neighbors

        def bfs(root):
            q = deque([root])
            
            clonedNode = {root.val: Node(root.val)}

            while q:
                node = q.popleft()
                for neighbor in getNeighbor(node):
                    if neighbor.val not in clonedNode:
                        clonedNode[neighbor.val] = Node(neighbor.val)
                        q.append(neighbor)
                # Add the neighbor to the current node's clone's neighbors list
                    clonedNode[node.val].neighbors.append(clonedNode[neighbor.val])
            return clonedNode[root.val]
        return bfs(node)
                        


        
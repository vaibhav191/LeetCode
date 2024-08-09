"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 1. Do a bfs starting node
        #   if node not in dictionary, add pair 'val: Node' to dic
        #   mark visited
        # 2. for each neighbor
        #   if neighbor not in dic, create node2
        #   add neighbor to the neighbor of node in dic
        #   if neighbor not in visited, add to q

        if not node:
            return
        if not node.neighbors:
            return Node(node.val)

        def bfs(root):
            clone = {}
            visited = set()
            q = deque()    
            q.append(root)
            visited.add(root.val)
            while q:
                n0 = q.popleft()
                if n0.val not in clone:
                    clone[n0.val] = Node(n0.val)
                for neighbor in n0.neighbors:
                    if neighbor.val not in clone:
                        clone[neighbor.val] = Node(neighbor.val)
                    clone[n0.val].neighbors.append(clone[neighbor.val])
                    if neighbor.val not in visited:
                        q.append(neighbor)
                        visited.add(neighbor.val)
            return clone
        return bfs(node)[node.val]


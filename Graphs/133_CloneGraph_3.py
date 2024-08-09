# No Hash
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
        old_to_new = [None]*101

        def dfs(node):
            if old_to_new[node.val] is not None:
                return old_to_new[node.val]
            copy = Node(node.val)
            old_to_new[node.val] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))        
            return copy

        return dfs(node) if node else None

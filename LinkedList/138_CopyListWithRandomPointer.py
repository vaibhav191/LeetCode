"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Map = {None: None}
        
        cur = head
        while cur:
            Map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = Map[cur]
            copy.next = Map[cur.next]
            copy.random = Map[cur.random]
            cur = cur.next
        return Map[head]

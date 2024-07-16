# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        deck = deque()
        if root:
            deck.append(root)
        while deck:
            rightSide = None
            for i in range(len(deck)):
                node = deck.popleft()
                if node:
                    deck.append(node.left)
                    deck.append(node.right)
                    rightSide = node
            if rightSide:
                res.append(rightSide.val)
        return res

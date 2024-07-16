# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        deck = deque()
        deck.append([root, root.val])
        good = 0
        while deck:
            node, maxv = deck.popleft()
            if node:
                if maxv <= node.val:
                    good += 1
                deck.append([node.left, max(maxv, node.val)])
                deck.append([node.right, max(maxv, node.val)])
        return good

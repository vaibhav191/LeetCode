# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        deck = deque()
        if not root:
            return []
        deck.append(root)
        while deck:
            localans = []
            for i in range(len(deck)):
                node = deck.popleft()
                if node:
                    deck.append(node.left)
                    deck.append(node.right)
                    localans.append(node.val)
            if len(localans): ans.append(localans)
        return ans

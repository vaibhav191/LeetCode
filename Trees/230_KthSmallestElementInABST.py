# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []
        list_ = self.bst2list(root)
        # print(self.l)
        return self.l[k - 1]
    
    def bst2list(self, root):
        if root:
            self.bst2list(root.left)
            self.l.append(root.val)
            self.bst2list(root.right)


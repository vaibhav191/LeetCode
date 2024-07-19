# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        route = []
        def dfs(root, s):
            s.append(str(root.val))
            if root.left is None and root.right is None:
                ans.append("->".join(s))
                return

            if root.left:
                dfs(root.left,s)
                s.pop()
            if root.right:
                dfs(root.right,s)
                s.pop()

        dfs(root, route)
        return ans

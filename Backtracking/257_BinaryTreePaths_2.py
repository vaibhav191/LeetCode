class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        route = []

        def dfs(root, s):
            if not root:
                return

            s.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->".join(s))
            else:
                dfs(root.left, s)
                dfs(root.right, s)

            s.pop()  # Backtrack

        dfs(root, route)
        return ans


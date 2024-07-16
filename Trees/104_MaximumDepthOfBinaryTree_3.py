class Solution:
    # iterative dfs
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(depth, max_depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return max_depth

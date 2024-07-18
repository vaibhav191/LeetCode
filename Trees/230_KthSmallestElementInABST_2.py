# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        ans = 0
        cur = root
        while stack:
            while cur.left:
                stack.append(cur.left)
                cur = cur.left
            while stack and not cur.right:
                op = stack.pop().val
                ans += 1
                if ans == k:
                    return op
                if stack:
                    cur = stack[-1]
            if stack and cur.right:
                op = stack.pop().val
                ans += 1
                if ans == k:
                    return op
                stack.append(cur.right)
                cur = cur.right
        return ans

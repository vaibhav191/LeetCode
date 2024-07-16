class Solution:
    # iterative bfs
    def maxDepth(self, root: TreeNode) -> int:
        deck = deque()
        if root:
            deck.append(root)
        level = 0
        while deck:
            for i in range(len(deck)):
                node = deck.popleft()
                if node.left:
                    deck.append(node.left)
                if node.right:
                    deck.append(node.right)
            level += 1
        return level

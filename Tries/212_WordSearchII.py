from typing import List
from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
    def add_word(self, w):
        curr = self
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r<0) or c< 0 or c == COLS or r == ROWS or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)

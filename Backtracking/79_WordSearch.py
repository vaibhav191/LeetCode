class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(row, col, i):
            if i == len(word):
                return True
            if (row not in range(ROWS)) or (col not in range(COLS)) or board[row][col] != word[i] or (row, col) in visited:
                return False
            visited.add((row, col))
            found = dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or \
                    dfs( row, col+1, i + 1) or dfs(row, col-1, i+1)
            visited.remove((row, col))
            return found

        count = Counter(word)

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        a = set(word)
        b = set()
        start_index = []
        ROWS = len(board)
        COLS = len(board[0])
        for i in range(ROWS):
            for j in range(COLS):
                if word[0] in board[i][j]:
                    start_index.append([i,j])
                b.add(board[i][j])
        
        if len(a-b)>0:
            return False

        def backtrack(r, c, string, used):
            if r < 0 or c < 0 or r>= ROWS or c >= COLS or tuple((r,c)) in used:
                return False
            if len(string) > 0 and string[-1] != word[len(string)-1]:
                return False
            if string + board[r][c]== word:
                return True
            used.add(tuple((r,c)))
            res = backtrack(r + 1, c, string + board[r][c], used)\
            or backtrack(r - 1, c, string + board[r][c], used)\
            or backtrack(r, c + 1, string + board[r][c], used)\
            or backtrack(r, c - 1, string + board[r][c], used)
            used.remove(tuple((r,c)))
            return res

        for i,j in start_index:
            if backtrack(i,j,"", set()):
                return True
        return False

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans, visited = set(), set()
        q = deque()
        ROWS, COLS = len(board), len(board[0])
        isvalid = lambda a,b: True if (0<=a<ROWS and 0<=b<COLS) else False
        for i in range(ROWS):
            if board[i][0] == 'O':
                ans.add((i, 0))
                q.append((i,0))
            if board[i][COLS-1] == 'O':
                ans.add((i, COLS-1))
                q.append((i, COLS-1))
        for i in range(COLS):
            if board[0][i] == 'O':
                ans.add((0, i))
                q.append((0, i))
            if board[ROWS-1][i] == 'O':
                ans.add((ROWS-1, i))
                q.append((ROWS-1, i))
        print(ans)
        while q:
            r, c = q.popleft()
            if (r,c) in visited:
                continue
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr,dc in directions:
                dr = r + dr
                dc = c + dc
                if isvalid(dr, dc) and board[dr][dc] == 'O' and (dr, dc) not in visited:
                    q.append((dr, dc))
                    ans.add((dr, dc))
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i,j) not in ans:
                    board[i][j] = 'X'
        return board
        

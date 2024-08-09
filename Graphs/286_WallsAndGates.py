class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dist = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        def addRoom(r, c):
            if (
                r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited
                or grid[r][c] == -1
            ):
                return
            q.append((r,c))
            visited.add((r,c))
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1

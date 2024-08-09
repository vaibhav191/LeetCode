class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        oranges = 0
        time = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    oranges += 1
        def add_loc(r, c):
            nonlocal oranges
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                grid[r][c] % 2 == 0 or
                (r, c) in visited
            ):
                return
            q.append((r, c))
            visited.add((r, c))
            oranges -= 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                add_loc(r - 1, c)
                add_loc(r + 1, c)
                add_loc(r, c - 1)
                add_loc(r, c + 1)
            time += 1
        return max(0, time - 1) if oranges == 0 else -1

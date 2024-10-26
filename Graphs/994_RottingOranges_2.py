from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    r_ = r + dr
                    c_ = c + dc
                    if 0<=r_<rows and 0<=c_<cols and grid[r_ ][c_ ] == 1:
                        grid[r_][c_] = 2
                        fresh -= 1
                        q.append((r_, c_))
            time += 1
        return time if not fresh else -1

if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    s = Solution()
    print(s.orangesRotting(grid)) # 4

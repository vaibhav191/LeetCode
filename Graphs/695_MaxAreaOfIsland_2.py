class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        visited = set()

        def bfs(r, c):
            if (r < 0
                or c< 0
                or r == rows
                or c == cols
                or grid[r][c] == 0
                or (r,c) in visited
                ):
                return 0
            visited.add((r,c))
            return 1 + bfs(r+1,c) + bfs(r-1,c) + bfs(r,c+1) + bfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, bfs(i,j))
        return ans

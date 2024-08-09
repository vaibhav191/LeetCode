class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        roots = set()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    roots.add((i, j))
        
        def bfs(r, c):
            r0, c0 = r,c
            d = deque()
            d.append((r, c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while d:
                r, c = d.popleft()
                for di, dj in directions:
                    ri, cj = r + di, c + dj
                    if ri>= 0 and ri < rows and cj>=0 and cj<cols and (r0,c0) != (ri,cj) and grid[ri][cj] =='1' and (ri,cj) not in visited:
                        roots.discard((ri,cj))
                        visited.add((ri,cj))
                        d.append((ri,cj))
        for r, c in list(roots):
            if (r, c) not in visited:
                bfs(r,c)
        
        return len(roots)

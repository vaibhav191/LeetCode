class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()
        roots = set()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    roots.add((i,j))
        
        def bfs(r, c):
            area = 1
            r0, c0 = r,c
            nonlocal ans
            d = deque()
            d.append((r,c))
            directions = [[1, 0], [-1,0],[0,1],[0,-1]]
            while d:
                r,c = d.popleft()
                for di, dj in directions:
                    ri, cj = r + di, c + dj
                    if ri<0 or cj<0 or  (ri,cj)==(r0,c0) or ri>=rows or cj>=cols or grid[ri][cj] == 0 or (ri,cj) in visited:
                        continue
                    area += 1
                    d.append((ri, cj))
                    visited.add((ri,cj))
            ans = max(ans, area)
        
        for ii, ij in list(roots):
            if (ii,ij) not in visited:
                bfs(ii, ij)

        return ans

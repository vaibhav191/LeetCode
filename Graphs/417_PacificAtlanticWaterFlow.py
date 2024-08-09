class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        def dfs(r, c, ocean, prevHeight):
            if (
                min(r,c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in ocean or
                heights[r][c] < prevHeight
            ):
                return
            ocean.add((r,c))
            dfs(r+1, c, ocean, heights[r][c])
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])

        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS-1, atl, heights[i][COLS-1])
        for i in range(COLS):
            dfs(0, i, pac, heights[0][i])
            dfs(ROWS-1, i, atl, heights[ROWS-1][i])            
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl: ans.append([i, j])
        return ans

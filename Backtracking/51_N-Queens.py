class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(r,c,ans):
            if len(ans) == n:
                res.append(ans.copy())
                return
            if len(ans) < r:
                return
            for i in range(r, n):
                for j in range(n):
                    if (i,j) not in ans and self.isValid(i, j, ans, n):
                        ans.add((i,j))
                        # print(ans)
                        backtrack(i+1, 0, ans)
                        ans.remove((i,j))
                if len(ans) != r+1:
                    return
        backtrack(0, 0,set())
        boards = []
        for ans in res:
            ans = sorted(ans)
            sub = []
            for r,c in ans:
                s = ''
                for i in range(n):
                    if i == c:
                        s+='Q'
                    else:
                        s+='.'
                sub.append(s)
            boards.append(sub)
        return boards

    def isValid(self, i, j, ans, n):
        r = i
        c = j
        # check vertical
        while r>0:
            if (r-1,c) in ans:
                return False
            r -= 1
        # check diagnol l
        r = i
        while r>0 and c>0:
            if (r-1, c-1) in ans:
                return False
            r -= 1
            c -= 1
        # check diagnol r
        r,c = i,j
        while r>0 and c<n-1:
            if (r-1, c+1) in ans:
                return False
            r -= 1
            c += 1
        return True

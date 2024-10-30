class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        ans = []
        part = []

        def backtrack(i):
            if i >= len(s):
                ans.append(part.copy())
            
            for j in range(i, len(s)):
                if isPali(i, j):
                    part.append(s[i:j+1])
                    # print(part)
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return ans

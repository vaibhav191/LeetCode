#TLE
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def permutes(s):
            if len(s) == 1:
                return [s]
            ans = []
            for i in range(len(s)):
                remaining_chars = s[:i] + s[i+1:]
                for perm in permutes(remaining_chars):
                    ans.append(s[i] + perm)
            return ans
        for permute in permutes(s1):
            if permute in s2:
                return True
        return False

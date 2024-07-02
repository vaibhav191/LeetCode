class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = [0] * 26
        maxf, ans = 0,0 
        while r<= len(s) - 1:
            count[ord(s[r]) - 65] += 1
            maxf = max(maxf, count[ord(s[r]) - 65])
            if (r-l+1)-maxf <= k:
                ans = max(ans, r-l+1)   
            else:
                count[ord(s[l]) - 65] -= 1
                l += 1
            r += 1
        return ans

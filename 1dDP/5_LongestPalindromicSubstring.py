# On^2 time, O1 space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxlen = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if r - l + 1> maxlen:
                    res = s[l:r+1]
                    maxlen = r - l + 1
                l -= 1
                r += 1
            # even
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if r - l + 1> maxlen:
                    res = s[l:r+1]
                    maxlen = r - l + 1
                l -= 1
                r += 1
        return res

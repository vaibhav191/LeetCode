from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_s = defaultdict(int)
        char_t = defaultdict(int)
        for i in range(len(s)):
            char_s[s[i]]+=1
            char_t[t[i]]+=1
        return char_s == char_t
        

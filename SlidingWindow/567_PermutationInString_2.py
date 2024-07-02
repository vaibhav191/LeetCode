class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1_count = Counter(s1) 
        s2_count = Counter(s2[:r+1])
        while r< len(s2) - 1:
            if s2_count == s1_count: return True
            r += 1
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            s2_count[s2[l]] -= 1
            l += 1
            
        return s1_count == s2_count

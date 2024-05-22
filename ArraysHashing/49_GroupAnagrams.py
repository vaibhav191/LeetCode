#O(n)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for s in strs:
            c = [0]*26
            for char in s:
                c[ord(char) - ord('a')] += 1
            group_anagrams[tuple(c)].append(s)
        return group_anagrams.values()

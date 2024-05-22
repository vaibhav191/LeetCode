#O(n)
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num]+=1
        
        freq = [[] for _ in range(len(nums)+1)]
        for val, count in counter.items():
            freq[count].append(val)
        
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for element in freq[i]:
                ans.append(element)
            if len(ans) == k:
                return ans

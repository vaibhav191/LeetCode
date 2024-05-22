#O(nlogn)
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num]+=1
        counter_inv = defaultdict(list)
        for key, val in counter.items():
            counter_inv[val].append(key)
        print(counter_inv)
        counter_inv_keys_sorted = list(counter_inv.keys())
        counter_inv_keys_sorted.sort(reverse = True)
        ans = []
        while len(ans) < k :
            count = counter_inv_keys_sorted.pop(0)
            for val in counter_inv[count]:
                ans.append(val)
        return ans

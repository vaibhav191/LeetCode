class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        pos = set()
        neg = set()
        ans = set()
        for i in nums:
            if i >=0:
                pos.add(i)
            else: 
                neg.add(i)
            counts[i] = counts.get(i,0) + 1
        if counts.get(0,0) > 2:
            ans.add((0,0,0))
        for i in neg:
            for j in pos:
                search = -1*(i+j)
                if search in counts:
                    if search == i or search == j:
                        if counts[search] == 1:
                            continue
                    ans.add(tuple(sorted([i,j,search])))
        return ans




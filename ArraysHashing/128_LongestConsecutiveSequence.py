class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxCount = 0
        
        # counting sequences, beats 32%
        # for num in nums:
        #     if num-1 not in num_set: # it is a starter
        #         length = 1
        #         while num+length in num_set:
        #             length+=1
        #         maxCount = max(length, maxCount)
        
        #taking number then checking how far left and how far right nums can go, and calculating range
        while num_set:
            n = num_set.pop()
            m = n - 1
            o = n + 1
            while m in num_set:
                num_set.remove(m)
                m -= 1
            while o in num_set:
                num_set.remove(o)
                o+=1
            maxCount = max(maxCount, o - m -1)    

        return maxCount
            

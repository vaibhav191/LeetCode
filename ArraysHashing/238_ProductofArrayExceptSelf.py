class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        # calculate pre
        pre = 1
        for i in range(len(nums)):
            ans.append(pre)
            pre = pre*nums[i]
        
        #calculate post
        post = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * post
            post = post*nums[i]
        
        return ans

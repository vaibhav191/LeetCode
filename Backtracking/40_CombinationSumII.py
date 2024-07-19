class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []

        def backtrack(i, subset, s):
            if s == target:
                ans.append(subset.copy())
                return
            if s > target or i >= len(candidates):
                return
            
            # select nums[i]
            subset.append(candidates[i])
            backtrack(i + 1, subset, s + candidates[i])
            subset.pop()
            # don't select nums[i]
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, subset, s)
        backtrack(0, [], 0)
        return ans

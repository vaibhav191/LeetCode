class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i, arr, s):
            if s == target:
                ans.append(arr.copy())
                return
            if i>=len(candidates) or s > target:
                return
            arr.append(candidates[i])
            dfs(i, arr, s + candidates[i])
            arr.pop()
            dfs(i+1, arr, s)

        dfs(0, [], 0)
        return ans

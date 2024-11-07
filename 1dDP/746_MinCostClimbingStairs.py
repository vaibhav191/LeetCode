# O n time, O 1 space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

# On time, On space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        for i in range(len(cost) - 1, -1, -1):
            memo[i] = cost[i] + min(memo[i+1], memo[i+2])
        # print(memo)
        return min(memo[0], memo[1])

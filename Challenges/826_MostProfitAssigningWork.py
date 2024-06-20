class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pair = sorted(zip(difficulty,profit))
        worker.sort()
        maxp = 0
        i = 0
        output = 0
        for w in worker:
            while i<len(pair) and w >= pair[i][0]:
                maxp = max(maxp, pair[i][1])
                i += 1
            output += maxp
        return output

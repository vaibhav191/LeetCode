#counting sort O(n+k)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        minh, maxh = min(heights), max(heights)
        heightMap = {}
        for h in heights:
            if h in heightMap:
                heightMap[h] += 1
                continue
            heightMap[h] = 1
        expected = [0]*len(heights)
        j=0
        count = 0
        for i in range(minh, maxh + 1):
            if i in heightMap:
                for j in range(j, j + heightMap[i]):
                    # print(j,i)
                    expected[j] = i
                    if expected[j] != heights[j]:
                        count += 1
                j += 1
        return count

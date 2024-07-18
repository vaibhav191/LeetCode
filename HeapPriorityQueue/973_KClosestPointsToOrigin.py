class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sq = lambda x,y: [-(x**2 + y**2), [x,y]]
        max_heap = [sq(x,y) for x,y in points]
        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        return [x[1] for x in max_heap]

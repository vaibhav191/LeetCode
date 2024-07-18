class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-v for v in count.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while q or max_heap:
            time += 1
            if max_heap:
                task = 1 + heapq.heappop(max_heap)
                if task:
                    q.append([task, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time

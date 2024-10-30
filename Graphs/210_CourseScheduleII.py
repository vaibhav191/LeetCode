class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
            if pre not in pre_map:
                pre_map[pre] = []
        output = []
        cycle = set()
        visited = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            output.append(crs)
            cycle.remove(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

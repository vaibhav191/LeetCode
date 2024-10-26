class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for course,pre in prerequisites:
            courseMap[course].append(pre)
            if pre not in courseMap:
                courseMap[pre] = []
        visit_course = set()
        def dfs(i):
            if i in visit_course:
                return False
            if courseMap[i] == []:
                return True
            visit_course.add(i)
            for pre in courseMap[i]:
                if not dfs(pre): return False
            visit_course.remove(i)
            courseMap[i] = []
            return True    

        for i in range(numCourses):
            if not dfs(i): return False
        return True

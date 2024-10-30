class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for nbor in adj[i]:
                if nbor == prev:
                    continue
                if not dfs(nbor, i):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n

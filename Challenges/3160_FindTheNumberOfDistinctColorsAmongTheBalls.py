class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_cache = defaultdict(list)
        index_map = defaultdict(int)
        ans = []
        for i, color in queries:
            if i in index_map:
                c_old = index_map[i]
                # change color_cache
                j = color_cache[c_old].index(i)
                color_cache[c_old][j], color_cache[c_old][-1] = color_cache[c_old][-1], color_cache[c_old][j]
                color_cache[c_old].pop()
                if len(color_cache[c_old]) == 0:
                    del color_cache[c_old]
            index_map[i] = color
            color_cache[color].append(i)
            ans.append(len(color_cache))
        return ans

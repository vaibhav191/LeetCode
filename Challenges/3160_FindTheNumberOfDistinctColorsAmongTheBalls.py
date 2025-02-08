class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_cache = defaultdict(int)
        index_map = defaultdict(int)
        ans = []
        for i, color in queries:
            if i in index_map:
                prev_color = index_map[i]
                if color_cache[prev_color] == 1:
                    del color_cache[prev_color]
                else:
                    color_cache[prev_color] -= 1
            index_map[i] = color
            color_cache[color] += 1
            ans.append(len(color_cache))
        return ans

class TimeMap:

    def __init__(self):
        self.dic = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic.setdefault(key, []).append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        l, r = 0, len(self.dic[key]) - 1 
        res = ""
        while l<=r:
            m = l + (r-l)//2
            if self.dic[key][m][0] <= timestamp:
                res = self.dic[key][m][1]
                l = m + 1
                continue
            r = m - 1
        return res
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

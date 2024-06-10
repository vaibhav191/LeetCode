class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force
        maxHeight = 0
        for i in range(len(height)):
            l = i
            r = l + 1
            while r<len(height):
                min_height = min(height[l], height[r])
                width = r - l
                area = width*min_height
                maxHeight = max(maxHeight, area)
                r += 1
        return maxHeight

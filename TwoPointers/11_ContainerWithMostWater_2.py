class Solution:
    def maxArea(self, height: List[int]) -> int:
        #O(n)
        max_area = 0
        max_height = max(height)
        l, r = 0, len(height)-1
        while l<r:
            area = min(height[l], height[r])*(r-l)
            max_area = max(max_area, area)
            # if the max area calculated = max height in the array * current width, then thats already the most
            # optimal possible area for that height and width and hence no need to calculate and check other loops
            if max_area >= max_height * (r-l):
                break
            if height[l] < height[r]:
                l += 1
            else:
                r-=1
        return max_area

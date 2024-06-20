class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = (position[-1]//(m-1))+1 # maximum gap between balls

        def canPlaceMballs(position, distance, m):
            prev_ball_loc = position[0]
            balls_placed = 1

            for i in range(1, len(position)):
                if position[i] - prev_ball_loc >= distance:
                    balls_placed += 1
                    prev_ball_loc = position[i]
                if balls_placed == m:
                    return True
            return False
        min_distance = 0
        while low<= high:
            mid = low + (high-low)//2
            if canPlaceMballs(position, mid, m):
                min_distance = mid
                low = mid + 1
            else:
                high = mid - 1
        return min_distance
        

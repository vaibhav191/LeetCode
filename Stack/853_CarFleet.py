class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import deque
        fleets = deque()
        for pos,spd in sorted(zip(position, speed), reverse = True):
            eta = (target - pos)/spd
            if not fleets or fleets[-1] < eta:
                fleets.append(eta)
        return len(fleets)

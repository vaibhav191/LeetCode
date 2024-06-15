#O(n + m), counting sort
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        m = max(students + seats)
        differences = [0] * m
        for stu in students:
            differences[stu-1] += 1
        for seat in seats:
            differences[seat-1] -= 1
        steps = 0
        unmatched = 0
        for i in range(len(differences)):    
            steps = steps + abs(unmatched)
            unmatched += differences[i]
        return steps

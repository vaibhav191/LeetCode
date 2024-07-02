class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        while i <= len(arr) - 3:
            if arr[i] % 2 == 1:
                if arr[i+1] % 2 == 1:
                    if arr[i+2] % 2 == 1:
                        return True
                    else:
                        i += 3
                else:
                    i += 2
            else:
                i += 1
        return False

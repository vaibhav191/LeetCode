class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l+r) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                lin = 0
                rin = len(matrix[m]) - 1
                row = m
                while lin<= rin:
                    m = (lin+rin)//2
                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] > target:
                        rin = m - 1
                    else:
                        lin = m + 1
                return False
            elif target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][0]:
                l = m + 1
            
        return False
        

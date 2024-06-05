class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            diff = target - numbers[i]
            print(i, diff)
            l = i+1
            r = len(numbers)-1
            while l<=r:
                m= (l+r)//2
                print(m)
                if numbers[m] == diff:
                    return [i+1, m+1]
                elif numbers[m] > diff:
                    r = m - 1
                else:
                    l = m + 1
        

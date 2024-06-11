class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        arr1 = []
        for num in arr2:
            for j in range(count[num]):
                arr1.append(num)
            del(count[num])
        sortednums = sorted(list(count.keys()))
        for num in sortednums:
            for j in range(count[num]):
                arr1.append(num)
        return arr1

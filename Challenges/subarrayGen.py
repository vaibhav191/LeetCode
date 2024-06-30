subs = []
        def genSubarrays(arr, start, end):
            if end == len(arr):
                return
            elif start > end:
                genSubarrays(arr, 0, end+1)
            else:
                subs.append(arr[start:end+1])
                return genSubarrays(arr, start + 1, end)
        
        genSubarrays(nums, 0, 0)
        

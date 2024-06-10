def three_sum(nums):
    nums.sort()  # Sort the array
    triplets = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate values

        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicate values
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicate values
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left
    
    return triplets


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = []
        current_number = 1

        for _ in range(n):
            nums.append(current_number)

            # multiply by 10 to get next lexi number
            if current_number *  10 <= n:
                current_number *= 10
            else:
                # increment by 1, as long as its not ending with 9 or greater than n
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10 # removing last digit
                current_number += 1
        return nums

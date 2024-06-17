# Define the list of numbers
numbers = '123'

# Function to generate combinations
def generate_combinations(numbers):
    length = len(numbers)
    result = []
    
    # Generate combinations for all lengths
    for i in range(2**length):
        combination = []
        for j in range(length):
            # If the j-th bit of i is set, add numbers[j] to the combination
            if (i >> j) & 1:
#                print(i, j, (i>>j), numbers[j])
                combination.append(numbers[j])
        result.append(combination)
    return result

# Get all combinations
all_combinations = generate_combinations(numbers)

# Print the formatted combinations
print(all_combinations)

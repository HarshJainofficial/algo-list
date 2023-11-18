#  Contain Duplicate  code in Python 
# This is famous leetcode problem

def contains_duplicate_bruteforce(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True

    return False

# Example usage
example1 = [1, 2, 3, 1]
result1 = contains_duplicate_bruteforce(example1)
print(f"Example 1: {example1}, Output: {result1}")

example2 = [1, 2, 3, 4]
result2 = contains_duplicate_bruteforce(example2)
print(f"Example 2: {example2}, Output: {result2}")

example3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result3 = contains_duplicate_bruteforce(example3)
print(f"Example 3: {example3}, Output: {result3}")

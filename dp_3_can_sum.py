# CAN WE GET THE SUM?
# Write a function 'can_sum(target_sum, numbers)' that takes in a
# target-sum and an array of numbers as arguments.
#
# The function should return a boolean indicating whether 
# or not it is possible to generate the target-sum using the numbers from the array.
#
# You may use an element of array as many times as needed.
# All input numbers should be assumed to positive.


# --------------------------------------
# A Brute force implementation
# Time Complexity: O(n^m)
# Space Complexity: O(m), as height of tree could be maximum 'm'
def can_sum_brute(target_sum, numbers):
    
    # Two Base conditions,
    # because we expect two types of output
    if target_sum == 0: 
        return True
    if target_sum < 0:  # When target-sum gets negative
        return False

    # For each number in numbers list,
    # check if subtracting it with target-sum leads us to a zero (0).
    for num in numbers:
        remainder = target_sum - num
        if can_sum_brute(remainder, numbers) == True:
            return True
    
    # Only after iterating through all numbers,
    # we can be sure that neither of them lead us to the target-sum
    return False


# --------------------------------------
# A DP implementation
# Time Complexity: O(m*n)
# Space Complexity: O(m)
def can_sum_dp(target_sum, numbers, cache = {}):
    
    # First check if desired target-sum's status(True/False) present in cache
    if target_sum in cache:
        return cache[target_sum]
    
    # Base conditions
    if target_sum == 0: return True
    if target_sum < 0: return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum_dp(remainder, numbers, cache) == True:
            # Saving to cache, when True
            cache[target_sum] = True    
            return cache[target_sum]
    
    # Saving to cache, when False
    cache[target_sum] = False   
    return cache[target_sum]


if __name__ == "__main__":
    
    print(can_sum_brute(7, [2, 3]))         # Output must be True.
    print(can_sum_brute(7, [5, 4, 3, 7]))   # Output must be True.
    print(can_sum_brute(7, [2, 4]))         # Output must be False.
    print(can_sum_brute(7, [2, 3, 5]))      # Output must be True.
    print(can_sum_dp(300, [7, 14]))         # Output must be False.
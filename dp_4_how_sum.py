# HOW DID WE GET THE SUM?
# Write a function 'how_sum(target_sum, numbers)' that takes in a
# target-sum and an array of numbers as arguments.
#
# The function should return an array containing any combination of
# elements that add up to exactly the target-sum.
#
# If there is no combination that adds up to the target-sum, then
# return null.
#
# If there are multiple combinations possible, you may return any single one.
#
# You may use an element of array as many times as needed.
# All input numbers should be assumed to positive.


# --------------------------------------
# A Brute force implementation
# Time Complexity: O(n^m * m), as the extra m comes from the maximum lenght(m) of the result_list
# Space Complexity: O(m), as height of tree could be maximum 'm'
def how_sum_brute(target_sum, numbers):
    
    # Base conditions,
    if target_sum == 0: return []   # A trivial case, will return [] i.e, empty list when target-sum is 0.
    if target_sum < 0:  return None # Indicates target-sum cannot be generated.

    for num in numbers:
        remainder = target_sum - num
        
        # This recursion call will always return a list of numbers
        #  from previous calls made so far.
        result_list = how_sum_brute(remainder, numbers)
        if result_list != None:
            return [num, *result_list]

    # Only after iterating through all numbers,
    # we want to be sure that neither of them lead us to the target-sum
    return None
    

# --------------------------------------
# A DP implementation
# Time Complexity: O(n*m * m)
# Space Complexity: O(m * m), as there could be "m" keys in cache with max. "m" length of list each
def how_sum_dp(target_sum, numbers, cache = {}):
    
    # First check if desired target-sum's list is present in cache.
    if target_sum in cache:
        return cache[target_sum]
    
    # Base conditions,
    if target_sum == 0: return []   
    if target_sum < 0:  return None

    for num in numbers:

        remainder = target_sum - num
        result_list = how_sum_dp(remainder, numbers, cache)

        if result_list != None:
            cache[target_sum] = [num, *result_list]     # Saving to cache
            return cache[target_sum]

    cache[target_sum] = None    # Saving to cache
    return cache[target_sum]


if __name__ == "__main__":
    
    print(how_sum_brute(7, [2, 3]))         # Output must be [2, 2, 3].
    print(how_sum_brute(7, [5, 4, 3, 7]))   # Output must be [4, 3].
    print(how_sum_brute(7, [2, 4]))         # Output must be None.
    print(how_sum_brute(7, [2, 3, 5]))      # Output must be [2, 2, 3].
    print(how_sum_dp(300, [7, 14]))         # Output must be None.
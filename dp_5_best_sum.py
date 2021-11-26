# WHAT BEST SUM WE CAN GET?
# Write a function 'best_sum(target_sum, numbers)' that takes in a
# target-sum and an array of numbers as arguments.
#
# The function should return an array containing the shortest
# combination of numbers that add up to exactly the target-sum.
#
# If there are multiple combinations possible, you may return any single one.
#
# You may use an element of array as many times as needed.
# All input numbers should be assumed to positive.


# --------------------------------------
# A Brute force implementation
# Time Complexity: O(n^m * m), as the extra m comes from the maximum lenght(m) of the result_list
# Space Complexity: O(m * m), as for each recursion, we may need at max "m" for storing the shortest_combination
def best_sum_brute(target_sum, numbers):
    
    # Base conditions
    if target_sum == 0: return []   # A trivial case, will return [] i.e, empty list when target-sum is 0.
    if target_sum < 0:  return None # Indicates target-sum cannot be generated.

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        
        # This recursion call will always return a list of numbers
        # from previous calls made so far.
        base_list = best_sum_brute(remainder, numbers)

        if base_list != None:
            # We need to store this combination so that we can make comparisons 
            # and find the shortest of them
            current_combination =  [num, *base_list]
            
            # If shortest found
            if shortest_combination == None or len(current_combination) < len(shortest_combination):
                shortest_combination = current_combination

    # Only after iterating through all numbers,
    # we want to be sure and return the shortest-combination
    return shortest_combination
    

# --------------------------------------
# A DP implementation
# Time Complexity: O(n*m * m)
# Space Complexity: O(m * m), as there could be "m" keys in cache with max. "m" length of list each
def best_sum_dp(target_sum, numbers, cache = {}):
    
    # First check if desired target-sum's shortest-combination is present in cache.
    if target_sum in cache:
        return cache[target_sum]
    
    # Base conditions,
    if target_sum == 0: return []   # A trivial case, will return [] i.e, empty list when target-sum is 0.
    if target_sum < 0:  return None # Indicates target-sum cannot be generated.

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        
        # This recursion call will always return a list of numbers
        # from previous calls made so far.
        base_list = best_sum_dp(remainder, numbers, cache)

        if base_list != None:
            # We need to store this combination so that we can make comparisons 
            # and find the shortest of them
            current_combination =  [num, *base_list]
            
            # If shortest found
            if shortest_combination == None or len(current_combination) < len(shortest_combination):
                shortest_combination = current_combination

    # Only after iterating through all numbers,
    # we want to be sure and return the shortest-combination
    cache[target_sum] = shortest_combination        # Saving to cache
    return cache[target_sum]


if __name__ == "__main__":
    
    print(best_sum_brute(7, [5, 4, 3, 7]))       # Output must be [7].
    print(best_sum_brute(8, [2, 3, 5]))          # Output must be [3, 5].
    print(best_sum_brute(8, [1, 4, 5]))          # Output must [4, 4].
    print(best_sum_dp(100, [1, 2, 5, 25]))       # Output must be [25, 25, 25, 25].
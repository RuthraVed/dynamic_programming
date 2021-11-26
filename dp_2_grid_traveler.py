# GRID TRAVELER PROBLEM
# Say that you are a traveler on a 2D grid.
# You begin in the top-left corner and 
# your goal is to travel to the bottom-right corner.
# Condition is that you can only move down or right.
#
# In how many ways can you travel to the goal on a grid with
# dimensions m x n?
# 
# Write a function 'grid_traveler(m,n)' that calculates this.


# --------------------------------------
# A Brute force implementation
# Time Complexity: O(2^n+m)
# Space Complexity: O(n+m)
def grid_traveler_brute(m, n):
    
    # Base conditions
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1

    # (m-1) indicates one step DOWN 
    # and (n-1) indicates one step RIGHT
    # Recursive call below gets us sum of moves made
    # i.e, all sub-DOWNs + all sub-RIGHTs
    return grid_traveler_brute(m-1,n) + grid_traveler_brute(m,n-1)


# --------------------------------------
# A DP implementation
# Time Complexity: O(n*m)
# Space Complexity: O(n+m)
def grid_traveler_dp(m, n, cache = {}):
    
    # Defining a key as string of "m,n"
    key = str(m) + "," + str(n)     
    
    # First check if desired (m, n) present in cache
    if key in cache:
        return cache[key]
    
    # Base conditions
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1

    # Make the Recursive call, save it in cache 
    # and then return the value from cache
    cache[key] = grid_traveler_dp(m-1, n, cache) + grid_traveler_dp(m, n-1, cache)
    return cache[key]


if __name__ == "__main__":

    print(grid_traveler_brute(3, 3))     # Output must be 6.
    print(grid_traveler_dp( 18, 18))        # Output must be 2333606220.

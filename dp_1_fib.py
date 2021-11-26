# FIBONACCI PROBLEM
# Write a function 'fib(N)' that takes in a number as an argument.
# The function should return the nth number of the Fibonnaci sequence.
#
# The 0th number of sequence is 0.
# The 1st number of sequence is 1.
#
# To generate the next number of the sequence,we sum the previous two.
#
# N     : 0, 1, 2, 3, 4, 5, 6, 7, ...
# fib(N): 0, 1, 1, 2, 3, 5, 8, 13, ...

# --------------------------------------
# A Brute force implementation
# Time Complexity: O(2^N)
# Space Complexity: O(N)
def fib_brute(N):
    # Base conditions
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # Recursive call
    return fib_brute(N - 1) + fib_brute(N - 2)

# --------------------------------------
# A DP implementation
# Time Complexity: O(N)
# Space Complexity: O(N)

def fib_dp(N, cache = {}):

    # First check if fib(N) present in cache
    if N in cache:
        return cache[N]

    # Base conditions
    if N == 0:
        return 0
    elif N == 1:
        return 1

    # Make the Recursive call, save it in cache 
    # and then return the value from cache
    cache[N] = fib_dp(N - 1, cache) + fib_dp(N - 2, cache)
    return cache[N]



if __name__ == "__main__":
    print(fib_brute(7))     # Output must be 13.
    print(fib_dp(50))     # Output must be 12586269025.
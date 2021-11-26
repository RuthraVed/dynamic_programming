# COUNT WAYS IN WHICH THE WORD CAN BE CONSTRUCTED?
# Write a function 'count_construct(target, word_bank)' that accepts a
# target string and an array of strings.
#
# The function should return the number of ways that the 'target' can
# 'target' can be constructed by concatenating elements of the 'word_bank' array.
#
# You may reuse elements of 'word_bank' as many times needed.

# --------------------------------------
# A Brute force implementation
# Time Complexity: O(n^m * m)
# Space Complexity: O(m^2)
def count_construct_brute(target, word_bank):
    
    # Base condition - If target is empty string
    # then there is atleast 1 way to create it.
    if target == "": return 1

    total_ways = 0  # To get us count from each word branch
    for word in word_bank:
        # We need to know if any word is a prefix 
        # of the target & save the suffix, i.e remaing part
        if target.startswith(word):
            suffix = target[len(word):]
            total_ways += count_construct_brute(suffix, word_bank)
    
    # Only after going through every word in word_bank,
    # we can be sure that we counted all the ways
    return total_ways

# --------------------------------------
# A DP implementation
# Time Complexity: O(n*m *m)
# Space Complexity: O(m^2)
def count_construct_dp(target, word_bank, cache = {}):
    
    # First check if target word's count in cache already
    if target in cache: return cache[target]

    # Base condition
    if target == "": return 1

    total_ways = 0  # To get us count from each word branch
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            total_ways += count_construct_dp(suffix, word_bank, cache)
    
    cache[target] = total_ways
    return cache[target]

if __name__ == "__main__":

    
    # Below output must be 2.
    print(count_construct_brute("purple", ["purp", "p", "ur", "le", "purpl"]))
    
    # Below output must be 1.
    print(count_construct_brute("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    
    # Below output must be 0.
    print(count_construct_brute("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    
    # Below output must be 4.
    print(count_construct_brute("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    
    # Below output must be 4602829.
    print(count_construct_dp("eeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eeee",
        "eeeeee",
        "eeeeeee",
        "f"
    ]))

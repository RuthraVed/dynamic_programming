# CAN THE WORD BE CONSTRUCTED?
# Write a function 'can_construct(target, word_bank)' that accepts a
# target string and an array of strings.
#
# The function should return a boolean indicating whether ot not the
# 'target' can be constructed by concatenating elements of the 'word_bank' array.
#
# You may reuse elements of 'word_bank' as many times needed.

# --------------------------------------
# A Brute force implementation
# Time Complexity: O(n^m * m), extra "* m" on branch, i.e word_bank iteration we save suffix
# Space Complexity: O(m^2)
def can_construct_brute(target, word_bank):
    # Base condition - If target is empty string
    # it's always possible to create.
    if target == "": return True

    for word in word_bank:
        # We need to know if any word is a prefix 
        # of the target & save the suffix, i.e remaing part
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct_brute(suffix, word_bank) == True:   
                return True     # Early return, if True.
    
    # Only after going through every word in word_bank,
    # we can be sure that target cannot be generated
    return False
    

# --------------------------------------
# A DP implementation
# Time Complexity: O(n*m *m)
# Space Complexity: O(m^2)
def can_construct_dp(target, word_bank, cache = {}):
    
    # First check if target word's status in cache already
    if target in cache: return cache[target]

    # Base condition
    if target == "": return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct_dp(suffix, word_bank, cache) == True:   
                cache[target] = True
                return cache[target]     # Early return, if True.
    
    cache[target] = False
    return cache[target]


if __name__ == "__main__":

    print(can_construct_brute("abcdef", ["ab", "abc", "cd", "def", "abcd"]))                    # Output must be True.
    print(can_construct_brute("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))     # Output must be False.
    print(can_construct_brute("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))   # Output must be True.
    print(can_construct_dp("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eeee",
        "eeeeee",
        "eeeeeee",
    ]))     # Output must be False.
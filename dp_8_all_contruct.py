# ALL THE WAYS TO CONSTRUCT THE WORD
# Write a function 'all_construct(target, word_bank)' that accepts a
# target string and an array of strings.
#
# The function should return a 2D array containing all of the ways
# that the 'target' can be constructed by concatenating
# elements of the 'word_bank' array.
#
# You may reuse elements of 'word_bank' as many times needed.

# --------------------------------------
# A Brute force implementation
# Time Complexity: O(n^m *m)
# Space Complexity: O(m*m*m)
def all_construct_brute(target, word_bank):
    # Base condition - If target is empty string
    # then there is always one empty list to create it.
    if target == "": return [[]]

    all_ways = []  # To get us combinations from each word branch
    for word in word_bank:
        # We need to know if any word is a prefix 
        # of the target & save the suffix, i.e remaing part
        if target.startswith(word):
            suffix = target[len(word):]
            
            # The recursion call will usually get [[]] or [] only, 
            # for each branch whose target can be created.
            # because it reaches till the leaf node of the tree.
            suffix_ways = all_construct_brute(suffix, word_bank)
            print(f'\t suffix_ways --> {suffix_ways}')
            
            if suffix_ways != []:

                # This variable helps us store the above child,
                # and it's preceding branch
                target_ways = list(map(lambda way: [word, *way], suffix_ways))
                print(f'\t target_ways --> {target_ways}')

                # Finally, we want to store all branch ways
                # only to be returned after full iteration.
                all_ways.extend(target_ways)
                print(f'\t all_ways --> {all_ways}')

    # Only after going through every word in word_bank,
    # we can be sure that we counted all the ways
    return all_ways

# --------------------------------------
# A DP implementation
# Time Complexity: O(n^m), we cannot do any better because we will anyways have to process n^m sub-arrays.
# Space Complexity: O(m)
def all_construct_dp(target, word_bank, cache = {}):
    
    # First check if target word's combination in cache already
    if target in cache: return cache[target]

    # Base condition
    if target == "": return [[]]

    all_ways = []  # To get us combinations from each word branch
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]   
            suffix_ways = all_construct_dp(suffix, word_bank, cache)
            
            if suffix_ways != []:
                target_ways = list(map(lambda way: [word, *way], suffix_ways))
                all_ways.extend(target_ways)

    cache[target] = all_ways
    return cache[target]

if __name__ == "__main__":

    print("Final result:", all_construct_brute("abc", ["a", "ab", "c"]))
    
    # Below output must be 2 [[], []] sub-arrays.
    print("Final result:", all_construct_brute("purple", ["purp", "p", "ur", "le", "purpl"]))

    # Below output must be 1 [[]] sub-array.
    print("Final result:", all_construct_brute("abcdef", ["ab", "abc", "cd", "def", "abcd"]))

    # Below output must be [].
    print("Final result:", all_construct_brute("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    
    # Below output must be 4 [[], [], [], []] sub-arrays.
    print("Final result:", all_construct_brute("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    
    # Below output must be [].
    print("Final result:", all_construct_dp("eeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eeee",
        "eeeeee",
        "eeeeeee",
    ]))

"""
Given a string representing a number, the goal is to find the highest possible palindrome that can be formed by changing at most 'k' digits in the string. A palindrome is a number that reads the same backward as forward. 

You are given a string 's' representing a number and an integer 'k'. The task is to find the highest palindrome that can be formed by changing at most 'k' digits in the string 's'.

Example:
Input:
s: 3943 
k: 1 
Palindrome:
1. 3943  => 3993
2. 3943 => 3443
Output: 3993
Explanation: Among the possible palindromes obtained, the highest palindrome is 3993 since 3993 > 3443.

"""


"""
# The Recursive Version!
# The recursive function 'helper' is used to find the highest palindrome that can be formed by changing at most 'k' digits in the string 's'. 
# The function takes the string 's', the number of changes 'k', and the indices 'left' and 'right' as arguments. 
# The function returns the highest palindrome that can be formed by changing at most 'k' digits in the string 's'.
"""
def highest_palindrome(s, k):
    def helper(s, k, left, right, changes):
        # Base case: if left crosses right, we are done
        if left > right:
            return ''.join(s) if k >= 0 else -1

        # If characters at the ends are not equal, make them equal and decrement or reduce k
        if s[left] != s[right]:
            # Set both to the higher value
            max_value = max(s[left], s[right])
            s[left] = s[right] = max_value
            changes[left] = changes[right] = 1
            k -= 1

        # If we run out of modifications, return -1
        if k < 0:
            return -1

        # Recursive call to process the next pair
        result = helper(s[:], k, left + 1, right - 1, changes[:])

        # If we have remaining modifications, try to maximize by making characters '9'
        if k > 0 and s[left] != '9':
            # Check if we can make both sides '9'
            if s[left] == s[right]:
                if changes[left] == 1 and changes[right] == 1:
                # If they are already equal, it will cost 2 modifications to change both to '9'
                    if k >= 1:
                        s[left] = s[right] = '9'
                        result = max(result, helper(s[:], k - 1, left + 1, right - 1, changes[:]))
                if k >= 2:
                    s[left] = s[right] = '9'
                    result = max(result, helper(s[:], k - 2, left + 1, right - 1, changes[:]))
            else:
                # If they are different, we have already spent one modification to make them equal
                # Making both '9' will cost one more modification
                s[left] = s[right] = '9'
                result = max(result, helper(s[:], k - 1, left + 1, right - 1, changes[:]))

        return result

    # Convert string to list to allow in-place modification
    # Convert string to list to allow in-place modification
    s = list(s)
    changes = [0] * len(s)  # Track changes made to each position
    return helper(s, k, 0, len(s) - 1, changes)

print(highest_palindrome("3943", 1)) # Output: 3993
print(highest_palindrome("932239", 2)) # Output: 992299
print(highest_palindrome("0011", 2)) # Output: -1
# Create more assert

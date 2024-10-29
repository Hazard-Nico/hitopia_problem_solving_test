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
# Looping Version!
# Loops through the string from the beginning and end, comparing the characters at each end. 
# If the characters are not equal, the character with the higher ordinal value is used to replace the other character. 
# The number of changes made is tracked by decrementing 'k'. If 'k' becomes negative, the function returns -1.
"""
def highest_palindrome(s, k):
    s = list(s)
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            s[i] = s[n-i-1] = max(s[i], s[n-i-1])
            k -= 1
    if k < 0:
        return -1
    i = 0
    while k > 0 and i < n//2:
        if s[i] != '9':
            if k >= 2 and s[i] == s[n-i-1]:
                s[i] = s[n-i-1] = '9'
                k -= 2
            elif k >= 1 and s[i] != s[n-i-1]:
                s[i] = s[n-i-1] = '9'
                k -= 1
        i += 1
    if n % 2 == 1 and k > 0:
        s[n//2] = '9'
    return ''.join(s)

print(highest_palindrome("3943", 1)) # Output: 3993
print(highest_palindrome("932239", 2)) # Output: 992299
print(highest_palindrome("0011", 2)) # Output: -1
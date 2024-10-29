"""
The Interview question:
The alphabet, from 'a' to 'z', is assigned weights corresponding to their ordinal positions. For instance, 'a' has a weight of 1, 'b' has a weight of 2, and so on, with 'z' having a weight of 26. The weight of a string is calculated by summing the weights of all its characters. Consider the string "gits" > gits = 7 + 9 + 20 + 19 = 55. Given a string, calculate its weight.
"""

"""
Example:
Given a string "abbcccd" and an array of queries "[1, 3, 9, 8]". 
The queries are used to determine the status of the numbers in the queries based on the following rules:
1. If a number in the queries is equal to the weight of a character or substring, return "Yes".
2. If a number in the queries is different from the weight of a character or substring, return "No".
a = 1
b = 2
bb = 4
c = 3
cc = 6
ccc = 9
d = 4 
Output: [Yes, Yes, Yes, No]
"""

def weighted_string(s, queries):
    weights = []
    for i in range(len(s)):
        if s[0] == s[i]:
            weights.append(ord(s[i]) - 96)
        else:
            if s[i] == s[i-1]:
                weights[-1] = weights[-1] + (ord(s[i]) - 96)
            else:
                weights.append(ord(s[i]) - 96)
    # print(weights)
    result = []
    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")
    return result

print(weighted_string("abbcccd", [1, 4, 9, 8])) # Output: [Yes, Yes, Yes, No]
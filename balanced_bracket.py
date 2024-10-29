"""
Given a string of brackets, determine whether it is balanced. The string may contain different types of brackets, including parentheses '()', square brackets '[]', and curly braces '{}'. 
The brackets may be separated by whitespace or not.

Example 1:
Input: { [ ( ) ] }
Output: YES
Explanation: Each bracket is balanced, with every opening bracket having a corresponding closing bracket of the same type.
opening : { }
opening : [ ]
opening : ( }

Example 2:
Input: { [ ( ] ) }
Output: NO
Explanation: The string { [ ( ] ) } is not balanced for the characters enclosed by the curly braces '{}', namely '[ ( ]'.

Example 3:
Input: { ( ( [ ] ) [ ] ) [ ] }
Output: YES
Explanation: Each bracket is balanced, with every opening bracket having a corresponding closing bracket of the same type, even though the bracket structure is irregular.
"""


# The Matching Bracket way!
def balanced_bracket(string):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    for char in string:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if stack == [] or matching_bracket[char] != stack.pop():
                return "No"
    return "Yes" if stack == [] else "No"
    
print(balanced_bracket("{ [ ( ) ] }")) # Output: True
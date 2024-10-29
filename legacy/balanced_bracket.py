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

"""
# The Iterative way!
# The function 'valid_braces' checks if the string of brackets is balanced.
"""

# def valid_braces(string):
#     stack = []
#     open_list = ["(", "[", "{"]
#     close_list = [")", "]", "}"]
#     for i in string:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False
# HITOPIA - Problem Solving Test

This repository is for my submission interview from GITS as my client. This contains solutions for the following three files:

1. **Question 1**: `weighted_string.py`
2. **Question 2**: `balanced_bracket.py`
3. **Question 3**: `highest_palindrome.py`

I also leave the legacy folder for my old ways.

## Question 1: `weighted_string.py`

### Description

The alphabet, from 'a' to 'z', is assigned weights corresponding to their ordinal positions. Given a string, calculate its weight.

### Example

```plaintext
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
```

### Solution

Using ord function for Unicode Conversion on strings and subtract with total of Unicodes (it was 96). The result is from the total of weight the character.

## Question 2: `balanced_bracket.py`

### Description

Given a string of brackets, determine whether it is balanced. The string may contain different types of brackets, including parentheses '()', square brackets '[]', and curly braces '{}'.
The brackets may be separated by whitespace or not.

### Example

```plaintext
Example 1:
Input: { [ ( ) ] }
Output: YES
Explanation: Each bracket is balanced, with every opening bracket having a corresponding closing bracket of the same type.
opening : { }
opening : [ ]
opening : ( }
```

### Solution

Using the dictionary value what we assigned of every opening bracket having a corresponding closing bracket of the same type. If not the same then take the dictionary keys and discard the value which is inconsistently.

## Question 3: `highest_palindrome.py`

### Description

Given a string representing a number, the goal is to find the highest possible palindrome that can be formed by changing at most 'k' digits in the string. A palindrome is a number that reads the same backward as forward.

You are given a string 's' representing a number and an integer 'k'. The task is to find the highest palindrome that can be formed by changing at most 'k' digits in the string 's'.

### Example

```plaintext
Input:
s: 3943
k: 1
Palindrome:
1. 3943  => 3993
2. 3943 => 3443
Output: 3993
Explanation: Among the possible palindromes obtained, the highest palindrome is 3993 since 3993 > 3443.
```

### Solution

- The recursive function 'helper' is used to find the highest palindrome that can be formed by changing at most 'k' digits in the string 's'.
- The function takes the string 's', the number of changes 'k', and the indices 'left' and 'right' as arguments.
- The function returns the highest palindrome that can be formed by changing at most 'k' digits in the string 's'.

## Contributing

This repository is public and contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

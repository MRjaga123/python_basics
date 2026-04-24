# Valid Number

# Companies
# Given a string s, return whether s is a valid number.
# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".
# Formally, a valid number is defined using one of the following definitions:
# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.
# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.
# The digits are defined as one or more digits.

# Example 1:
# Input: s = "0"
# Output: true
# Example 2:
# Input: s = "e"
# Output: false
# Example 3:
# Input: s = "."
# Output: false

# Constraints:
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

# Example 1:
# Input: s = "aacecaaa"Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"Output: "dcbabcd"

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only

# You are given a 0-indexed array of unique strings words.
# A palindrome pair is a pair of integers (i, j) such that:
# 0 <= i, j < words.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a palindrome.
# Return an array of all the palindrome pairs of words.
# You must write an algorithm with O(sum of words[i].length) runtime complexity.

# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]Output: [[0,1],[1,0],[3,2],[2,4]]Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
# Example 2:
# Input: words = ["bat","tab","cat"]Output: [[0,1],[1,0]]Explanation: The palindromes are ["battab","tabbat"]
# Example 3:
# Input: words = ["a",""]Output: [[0,1],[1,0]]Explanation: The palindromes are ["a","a"]

# Constraints:
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lowercase English letters.

###valid number

# "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"
# "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"

def validnumber(i:str) -> bool:
    a=i.strip()
    num=False
    sign=False
    dot=False
    e=False
    num_after_e=False
    for x,y in enumerate(a):
        if y.isdigit():
            num=True
            if e:
                num_after_e=True
        elif y in "Ee":
            if e or not num:
                return False
            e=True
            num_after_e=False
        elif y in "+-":
            if sign :
                return False
            sign=True
            num_after_e=True
        elif y in ".":
            if dot :
                return False
            dot=True
            num_after_e=True
        else:
            return False
    if a.isdigit():
        return num
    else:
        return num and num_after_e
inputs="+6e-1"
print(validnumber(inputs))

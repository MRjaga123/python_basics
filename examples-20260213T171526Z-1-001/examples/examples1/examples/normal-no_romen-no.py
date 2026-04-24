"""normal numbers to romen numbers"""
# 1. Integer to Roman Conversion
# - Problem: Given an integer (1 ≤ n ≤ 3999), convert it into a Roman numeral.
# - Twist: You must handle subtractive notation correctly (e.g., 4 → IV, 9 → IX, 40 → XL).
# - Example:
# Input: 1994 → Output: "MCMXCIV"

dicts={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

inputs=[1994]

for i in range(len(inputs)):
    for j in range(len(dicts.values())):
        print(j)

    print(i)
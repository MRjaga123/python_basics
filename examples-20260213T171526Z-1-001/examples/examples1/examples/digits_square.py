# 2.Replace Each Digit With Its Square
# For every digit in the string, replace it with digit².
# Keep alphabets unchanged.
# Example:
# Input: "a2b3c1"
# Output: "a4b9c1"

inputs = "a2b3c1"

for i in inputs:
    if i.isdigit():
        print(int(i)**2,end="")
    else:
        print(i,end="")

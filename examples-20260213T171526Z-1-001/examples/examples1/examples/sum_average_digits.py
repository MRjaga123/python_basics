# 1.Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
# Example:
# input:
# str1 = "PYnative29@#8496"
# output:
# Sum is: 38 Average is  6.333333333333333


str1="PYnative29@#8496"

sums=0
count=0
for i in str1:
    if i.isdigit():
        count+=1
        sums+=int(i)
print(sums)
print(count)

average=sums/count
print(average)

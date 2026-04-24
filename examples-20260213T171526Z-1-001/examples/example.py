#

def print_star_diagram(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()

    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()

    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()

    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n):
            print("*",end=" ")
        print()

    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1-1):
            print("*",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()

    for i in range(n-1):#diamond
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i+1-1):
            print("*",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(n-i-1):
            print("*",end=" ")
        for i in range(n-i):
            print("*",end=" ")
        print()

    for i in range(n):#
        for j in range(i+1):
            print("*",end=" ")
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        for j in range(i+1-1):
            print(" ",end=" ")
        for j in range(i+1-1):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")
        print()
size = 5
print_star_diagram(size)

#batman diagram
J=3
A=9
print()
for i in range(J):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(J-i):
        print(" ",end=" ")
    for j in range(0,J):
        print(" ",end=" ")
    for j in range(i+1-1):
        print("*",end=" ")
    for j in range(J-i):
        print(" ",end=" ")
    for j in range(J-i):
        print(" ",end=" ")
    for j in range(i+1-1):
        print("*",end=" ")
    for j in range(0,J):
        print(" ",end=" ")
    for j in range(J-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(A):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(A-i):
        print("*",end=" ")
    for j in range(A-i):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    print()

###############################
#find add or even
number=int(input("enter the number:"))
if number%2==0:
    print("it is even")
else:
    print("it is odd")

#find last number in digit
enter=int(input("enter total numbers to enter:"))
a=[]
for i in range(enter):
    x=int(input("enter the number:"))
    a.append(x)
print(a[-1])

enter=input("enter total numbers to enter:")
enter1=int(enter)
print(enter[-1])

#count digits in a number
enter=input("enter the numbers:")
count=0
for i in enter:
    count+=1
print(count)

#reverse the number
reverse=input("enter the reverse numbers:")
revrese1=int(reverse[::-1])
print(revrese1)

#find power of number
x=int(input("enter x:"))
y=int(input("enter y:"))
print("result:",pow(x,y))

#find gcd(greatest common divisor)
import math
a=int(input("enter a:"))
b=int(input("enter b:"))
print("result:",math.gcd(a,b))

#print all divisor of a number
n=12
for i in range(1,n+1):
    if i%n==0:
        print(i)

#
#formatting string

text=f"hi iam jaga 21"
print(text)

#placeholder{} and modifier:
price=100
text=f"my price is {price}" #placeholder{}
print(text)

price=100
text=f"my price is {price:.2f}" #modifier:
print(text)

#math operation
text=f"2 plus 2 is {2+2}" 
print(text)

price=10
tax=2
text=f"my total is {price+(price-tax)}"
print(text)

#if else
price=50
text=f"the price is {'expensive' if price>40 else 'cheap'}"
print(text)

#function
name="jaga"
text=f"my name is {name.upper()}"
print(text)

def function(x):
    return x * 10
text=f"my output is {function(10)}"
print(text)

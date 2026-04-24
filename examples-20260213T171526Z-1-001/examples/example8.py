#
"""
x=input("enter the input:")
y=eval(x)
"""

def precedence(op):
    if op in ('*','/'):
        return 2
    if op in ('+','-'):
        return 1
    return 0
    
def apply_op(a,b,op):
    if op == '*':
        return a*b
    if op == '/':
        return a/b
    if op =='+':
        return a+b
    if op =='-':
        return a-b
    
def evaluate(expression):
    values=[]
    ops=[]

    i=0
    while i<len(expression):
        if expression[i]==' ':
            i+=1
            continue

        if expression[i].isdigit():
            val=0

            while i<len(expression) and expression[i].isdigit():
                val=int(expression[i])
                i+=1
            values.append(val)
            continue

        if expression[i] in "*/+-":
            while ops and precedence(ops[-1]) >= precedence(expression[i]) :
                b=values.pop()
                a=values.pop()
                op=ops.pop()
                values.append(apply_op(a,b,op))
            ops.append(expression[i])
        i+=1
    while ops:
        b=values.pop()
        a=values.pop()
        op=ops.pop()
        values.append(apply_op(a,b,op))
    return values[-1]    

i=input("enter :")
result=evaluate(i)
print("result:",result)



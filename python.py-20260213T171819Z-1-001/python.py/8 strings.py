print("jaga")

#quotes inside quotes
a="jaga'd'"
print(a)

#multiline string
x=""" jaga,
jaga,
jaga."""
print(x)

#strings are arrays
A="Jaga"
print(A[0])

#looping in string
for i in "zoro":
    print(i)

#length of string
print(len(A))

#check the string
print("a" in A) #in
print("e" not in A) #not in

#use if to check the string
if "a" in A:         #if in
    print("yes")

if "e" not in A:      #if not in
    print("no")

#slicing strings
name=" jaga,jaga"

print(name[0:1])#slice

print(name[:2]) #slice from start

print(name[2:]) #slice to end

print(name[-4:-1]) #negative indexing

#modify the string
print(name.upper()) #upper case
print(name.lower()) #lower case

print(name.strip()) #remove whitespace from start and end

print(name.replace("a","o")) #replace a for o

print(name.split(","))  #split the string

#concatenate
name1="zoro"
name2=name+" "+name1 #concatenate 
print(name2)

#f string
age=21
print(f"jaga,{age}") 

print(f"jaga,{age:.2f}") #2 decimal

print(f"jaga,{age*2}")   #math operations

#escape character \
txt="myself \"jaga\" from thanjai"
print(txt)

txt1="myself \\jaga"  #for backslash
print(txt1)

txt2="myself \n jaga" #newline \n
print(txt2)

txt3="myself\tjaga"   #tab
print(txt3)

txt4="myself \bjaga"  #remove backspace
print(txt4)



#string method

method="jaga"

print(method.capitalize())  #converts first character to upper case

print(method.casefold())    #converts string into lower case

print(method.center(20))    #returns a centered string

print(method.count("a"))    #count

print(method.encode())      #returns encode version of string

print(method.endswith(".")) #returns true if the string ends with specific value

print(txt3.expandtabs(100))  #set tab size of string

print(method.find("g"))     #find the position of the string

method1="jaga{age}thanjai"
print(method1.format(age=21))  #format specific value in string

myvar={"name":"jaga","age":21}
method2="my name is {name} my age is {age}" #format specific values from dictionary in string
print(method2.format_map(myvar))

print(method2.index("a",0,5))   #find the position of the string like (find method)

print(method.isalnum())  #return true if all characters are alphanumeric

print(method.isalpha())  #return true if all characters are alphabet

print(method.isascii())  #return true if all characters are ascii characters

print(method.isdecimal()) #return true if all characters are demical numbers

print(method.isdigit()) #return true if all characters are digit

print(method.isidentifier()) #return true if all characters in string is valid character

print(method.islower()) #return true if all characters are lower case

print(method.isnumeric()) #return true if all character are numeric

print(method.isprintable()) #return true if all characetrs in string are printable

print(method.isspace()) #return true if all characters in string are whitespace

print(method.istitle()) #return true if string follow the tittle rule

print(method.isupper()) #return true if all charater in string are upper case

print(" zoro ".join(method)) #join  in middle of all characters


method3=" jaga  "
meth3=method3.ljust(10,"*")  #returns left justified version string
print(meth3,"zoro zoro")

print(method3.lower())    #convert into lower case
print(method3.upper())    #convert into upper case

method4=",,,,,,.....     jaga   "
print(method4.lstrip(",,,... "))   #remove leading characters and spaces in left of side string

print(method3.strip())             #remove space from front and end

method5="one one one two two one"
print(method5.replace("one","three",2)) #replace the characters in string

method6="myself jaga from thanjai"   #split the characters and put it into list
print(method6.split())

method7="MySeLf"
print(method7.swapcase())      #convert lower into upper and upper into lower

method8 = "Good night son!"          #maketrans and translate
x = "nSo"
y = "uSu"
z = ""
mytable = str.maketrans(x, y, z)
print(method8.translate(mytable))

print(method8.zfill(20))  #fill the strings with 0 until it become 20characters

# numeric types of datatype

# it is of 3 types
# int
# float
# complex 

# int
a=10
print(a)
print(type(a)) # <class 'int'>

# when we supposed to get the type of a variable then we can do it by using type() function

# binary, hexadecimal, octadecimal representation of int
#  always integer type of variables are converted to binary, hexdecimal and octadecimal types

# binary representation
# it is very simple by calling bin() function

a=123
b=bin(a)
print("the binary representation of a is : ",b)
# output -- 0b1111011
# 0b -- binary representation

# hexadecimal
a=123
b=hex(a)
print("the hexa representation of a is : ",b)
# 0x7b
# 0x -- hexa representation

# octa representation
a=123
b=oct(a)
print("the octa representation of a is : ",b)
# 0o --- octa representATION
# 00173

# notes
# for converting int to binary ---- bin()
# for converting int to hexa ---- hex()
# for converting int to octa ---- oct()


# float
x=10.78
print(x)
print("type of x is :",type(x))

# how to convert a float number into integer --- by calling int()
y=int(x)
print(y) #10
# when we convert the floating point into integer the floating point numbers after point representation will
#  be ignored
print("type of y is :",type(y))
z=float(y)
print(z)
print("type of z is :",type(z))

# complex
# this format is defined as a+bj
# the value of j is square root of -1
a = 10+12j
print(a)
print("type of a is :",type(a))

b=-2-9j
print(b)
print("type of b is :",type(b))

c=a+b
print(c)
print("type of c is :",type(c))
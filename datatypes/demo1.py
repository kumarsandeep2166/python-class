a = [10,20,15,45,25,36,90,58,96,87,36]
x = bytearray(a)
# by calling bytearray() and passing "a" as argument to convert a into bytearray x
print(x[0])
print(x[4])
# print(x[7])incase of bytearray we can use or do the operations of item assignment
x[0] = 23
x[1] = 23
x[2] = 23
x[3] = 23
x[4] = 23
x[5] = 23
x[6] = 23
print("--------------------")
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])
print(x[6])
print("--------------------")
print('extract each item')
for i in x:
    print(i)
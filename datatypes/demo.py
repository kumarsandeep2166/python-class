# a --- list here
a = [10,20,15,45,25,36,90,58,96,87,36]
# a is converted into bytes
x = bytes(a)
# now by calling bytes() we can convert it into bytes
# in any type of sequence the index plays an important role and it starts from 0
print(x[0])
print(x[1])
print(x[2])
print(x[3])
# print(x[11]) # error
# because the last index which can be accessed is 10
# x[0]=11
# print(x[0])
# TypeError: 'bytes' object does not support item assignment
print("------------------")
print('Extract each items from bytes')
for i in x:
    print(i)

x[0]=12
print(x[0])

# TypeError: 'bytes' object does not support item assignment


# in java for loop is like the following
# for(int i=0; i<5; i++)
# {
#     System.out.println(x[i]);
# }
# bytes doesnot support item assignment
# we caanot replace a value from a particular place to another value

# for loop syntax
# for -start
# increment or decrement variable
# in -- operator
# destination
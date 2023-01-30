'''
Write python program to count the number of characters (character frequency) in a string.
'''
'''
s=input("Enter string:")
ch=0
n=0
for i in s:
    if i.isalpha():
       ch=ch+1
    elif i.isnumeric():
         n=n+1
print("total character :",ch)
print("total numeric :",n)

'''
'''

s=input("entre string")
ch=0
for i in s:
    if i.isalnum():
        ch=ch+1
print("total character :",ch)

'''

s=input("entre string: ")
ch=0
n=0
for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isnumeric():
        n=n+1
print("total character:",ch)
print("total number:",n)



'''
s=input("input string:")
ch=0
w=1
sp=0
n=0
special=0
for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
       sp=sp+1
       w=w+1
    elif i.isnumeric():
        n=n+1
    else:
      special=special+1

print("total special:",special)
print("total character:",ch)
print("total word:",w)
print("total space:",sp)
print("total number:",n)
'''
'''
Write python program to count the occurence of each word in a given sentence.
'''

'''
str=input("Enter string :")
str=str.split()
print(str)

i=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i],"present",count,"times")

    i=i+1
'''

s=input("Enter string:")
a=s.split(" ")
print(a)
i=0
while i<=len(a):
    count=1
    for j in a:
        if j==a[i]:
            count=count+1

    print(a[i],"present",count,"times")
    i=i+1

'''
str = "To change the overall look your document. To change the look available in the gallery"
c = dict()
txt = str.split(" ")
for t in txt:
    if t in c:
        c[t] += 1
    else:
        c[t] = 1
print(c)
'''



# problem we write 2 patel then output gives patel 2 times and patel 2 time how can we solve this pro to only one patel 2 time printed.

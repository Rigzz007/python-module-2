'''
Write python function that takes a list of words and return the length of the longest one.
'''
#complete

def longest_list(b):
    max1=len(s[0])
    temp=s[0]
    for i in s:
        if (len(i)>max1):
            max1=len(i)
            temp=i
    print("The word with the longest is:",temp,"and length is:",max1)
#a=["abc","cdsa","asdef"]
#print(longest_list(a))
#a=input("enter the string:")
s=[]
i=0
while i<5:
    a=input("enter the string:")
    s.append(a)
    i=i+1
print(s)
longest_list(s)





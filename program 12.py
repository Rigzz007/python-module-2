'''
Write python program to count occurrences of a substring in a string.
'''
'''
#s="My name is Rignesh patel.My father name is mukeshbhai patel.my mother name is bhanuben patel "
#a="patel"
s=input("Enter  string:")
a=input("Enter sub string:")
print(s.count(a))
'''
x=0
l=[]
m=[]

while x<5:


    s=input("Enter String : ")

    x=x+1
    l.append(s)
a=input("Enter Sub String :")


m.append(a)
print(l)
print(m)

#i=0
count=0
for i in l:
    for j in m:
        if i==j:
            count=count+1
            #print("occurrence is:",count)
            #j=j+1
            #i=i+1




#else:
#    print("occurrence is:",False)
    #pass
print("Occurrence of substring  is:",count)
#print(l)
#print(m)


#problem



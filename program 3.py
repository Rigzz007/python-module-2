'''
Write a python program to get the factorial series of given range.
'''
#complete
'''
n=int(input("Enetr a number :"))
a,b=0,1
while b<n:
    print(b,end=" ")
    a,b=b,a+b
'''
n=int(input("Enetr a number :"))
l=[]
r=[]
factorial=1
for i in range(1,n+1):
    l.append(i)
print("Range of nymbers which you want to factorial:",l)

#if l[i]>1:
for i in range(1,n+1):
    factorial=factorial*i
    #i=i+1
    r.append(factorial)

print("Factorial number of the given range is :",r)



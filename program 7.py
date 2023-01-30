'''
Write python program to sum of three given integers. However, if two values are equal sum will be zero.
'''
#1)
'''
a=int(input("Enter  number A:"))
b=int(input("Enter  number B :"))
c=int(input("Enter  number C:"))

if a==b:
    print("a and b is eqaul to",0)
elif b==c:
    print("b and c is eqaul to",0)
elif a==c:
    print("a and c is eqaul to",0)

else:
    print("a and b and c sum is",a+b+c)

'''
#2)

A=int(input("Enter  number A:"))
B=int(input("Enter  number B :"))
C=int(input("Enter  number C:"))
D=0
if A==B or A==C or B==C:
    print("Output of given three values are zero")
else:
    D=A+B+C
    print("Output of given three values are:",D)



'''
Write python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''
'''
a=int(input("Enter number A:"))
b=int(input("Enter number B:"))

if a==b:
    print("return True")
elif a+b==5:
    print("return True")
elif a-b==5:
    print("return True")
else:
    print("False")

'''
'''
A=int(input("Enter number A:"))
B=int(input("Enter number B:"))

if A==B or A+B==5 or A-B==5:
    print("True")
else:
    print("False")
'''
'''
A=int(input("Enter number A:"))
B=int(input("Enter number B:"))
C=0
D=0
C=A+B
D=A-B
if A==B:
    print("True")
elif C==5:
    print("True",C)
elif D==5:
    print("True",D)
else:
    print("False")
'''

'''
A=int(input("Enter number A:"))
operator = input("Choose operator(+,-)")
B=int(input("Enter number B:"))
C=0
D=0
if A==B:
    print("Two values are same",True)
elif operator == "+":

    C=A+B
    if C%5==0:
        print("Sum of two values  are true",C)
    else:
        print("Sum of two values are false",C)
elif operator == "-":

    D=A-B
    if D%5==0:
        print("Difference of two values are True",D)
    else:
        print("Difference of two values are False",D)

else:
    print("Output is:",False)
'''
A=int(input("Enter number A:"))
B=int(input("Enter number B:"))
C=0
D=0
if A==B:
    print("Two values are same",True)
else:
    operator = input("Choose operator(+,-)")

    if operator == "+":

        C=A+B
        if C%5==0:
            print("Sum of two values  are true",C)
        else:
            print("Sum of two values are false",C)
    elif operator == "-":

        D=A-B
        if D%5==0:
            print("Difference of two values are True",D)
        else:
            print("Difference of two values are False",D)

    else:
        print("Output is:",False)


'''
first =input("enter first number:")
operator = input("entre operator(+,-,*,/,%,**)")
second = input("entre second operator:")
first=int(first)
second=int(second)
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "/":
    print(first/second)
else:
    print("invalid operation")
'''


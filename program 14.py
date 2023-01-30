'''
Write python program to get a single string from two given strings, seperated by a space and swap the first two characters of each strings.
'''
#complete

A=input("Enter frist string:")
B=input("Enter second string:")
#C=A+" " + B
#print(C)
#D=C.split(" ")
#print(D)
#C=A[:2]+B[2:]
#print(C)
#D=B[:2]+A[2:]
#print(D)
#E=C+" "+D
#F=E.split(" ")
#print(F)

x=A[0:2]
A=A.replace(A[:2],B[:2])
B=B.replace(B[:2],x)
C=A+ " " +B
print(C)
D=C.split(" ")
print(D)


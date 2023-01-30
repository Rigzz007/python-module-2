'''
Write a python program to get the factorial number of given number.
'''
n=int(input("Enter the number of which you want to factorial:"))
factorial=1
if n>0:
    for i in range(1,n+1):
        factorial=factorial*n
        n=n-1
print("Factorial number of this number is:",factorial)







'''
Write python program to sum of the first n positive integers.
'''

sum=0
A=1
n=int(input("Enter a number :"))
for i in range(1,n+1):
      sum=sum+A
      A=A+1
print("sum of the n number is :",sum)


'''
Write python program to get a string made of the first 2 and the last 2 chars from a given a string.
 if the string length is less than 2, return insted of the empty string.
'''
#complete
'''
def fun(s):
    if len(s) < 4:
        #print(" ")
        return " "
    #else:                        # if we right if else then both return somthing we can not write return in only one condition.
    return   s[:2]+s[-2:]
        #print(s)

a=input("Enter a string:")
print("New string is :",fun(a))
#print(fun(a))
#fun(a)
'''

def fun(s):
    if len(s) < 4:
        #print(" ")
        return " "
    else:
       return   s[:2]+s[-2:]


a=input("Enter a string:")
print("New string is :",fun(a))
#print(fun(a))
#fun(a)



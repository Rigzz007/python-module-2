'''
Write python function to reverses a string if its length is a multiple of 4.
'''


def reverse_string(str1):
    if len(str1)%4==0:
        #return ""+(reversed(str1)) #can only concatenate str (not "reversed") to str
         return "".join(reversed(str1))
    return str1
a=input("enter string:")
print(reverse_string(a))



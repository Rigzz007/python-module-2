'''
Write python function to insert a string in the middle of a string.
'''
#complete
'''
def fun(c,d):
    p=len(c)//2
    f=c[:p] + d + c[p:]    #if we want to add middle of the string like string / 2
    print(f)

a=input("Enter string:")
b=input("Enter string which you want to add middle:")
print(fun(a,b))
'''
def fun(c,d):
    e=c.find("patel")
    f=c.find("mukeshbhai")
    g=c[e:f] + d + " " + c[f:]    #if we want to add some string at desire place of the string
    print(g)

#a=input("Enter string:")
#b=input("Enter string which you want to add middle:")
a="patel mukeshbhai"
b="rignesh"
print(fun(a,b))



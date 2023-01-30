'''
Write python program to add 'ing' at the end of a given string(length should be at least 3).
If the given string already ends with 'ing' then add 'ly' insted if the string length of the given string is less than 3, leave it unchanged.
'''
#complete
'''
s=input("Enter string:")
l=len(s)
if l>=3:
    if s[-3:]=="ing":
        s=s+"ly"
    else:
        s=s+"ing"
print(s)
'''

s=input("Enter string:")
l=len(s)
if l>=3:
    if s[-3:]=="ing":
       # s=s.replace(s[-3:],"ly") #this method use only to replace last ing into ly.
       s=s.replace("ing","ly")    # this method use to replace every ing into ly.
       print(s)
    else:
        s=s+"ing"
        print(s)





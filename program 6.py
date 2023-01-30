'''
Write python program to test whether a passed letter is a vowel or not.
'''
'''
#1)
s=input("enter the string:")
vowel=0
consonant=0
for i in s:                            #NOTE
    if(i=="A" or"E"or"I"or"O"or"U"):        #this type of method is not working
        vowel=vowel+1
    else:
        consonant=consonant+1
print("number of vowel",vowel)
print("number of consonant",consonant)
'''
#2)
s=input("enter the string:")
vowel=0
consonant=0
for i in s:
    if(i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="a"or i=="e"or
    i=="i"or i=="o"or i=="u"):
        vowel=vowel+1
    else:
        consonant=consonant+1
print("number of vowel",vowel)
print("number of consonant",consonant)

#3)
'''
s=input("enter the string:")
vowel=0
consonant=0
for i in s:
 if i in("A","E","I","O","U","a","e","i","o","u"):
    vowel=vowel+1
 else:
    consonant=consonant+1
print("number of vowel is:",vowel)
print("number of consonant:",consonant)
'''

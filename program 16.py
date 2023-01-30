'''
Write python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

#complete
#s="this man is  not poor "
s=input("Enter string:")
if s:
    f_not=s.find("not")      #this find function  return index of the  word like not and poor in given string.
    print(f_not)
    f_poor=s.find("poor")
    print(f_poor)
else:
    print(s)
if f_not<f_poor:
    print(s.replace("poor","good"))
else:
    print(s)




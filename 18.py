'''
Write a function called first_diff that is given two strings and
returns the first location in which the strings differ.
If the strings are identical, it should return -1.
'''
def first_diff(s1,s2):
    if(s1==s2):
        return -1
    else:
       if len(s1)==len(s2):
          for i in range(len(s1)):
              if s1[i]!=s2[i]:
                  return (i+1)     
    
s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
x=first_diff(s1,s2)
if(x== -1):
    print("strings are identical")
else:
    print("first difference occurs at location :",x)

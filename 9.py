a=input("enter a string ")

b=input("enter another string ")

n=""

if(len(a)!=len(b)):

 print("Different length")

else:

 for i in range(0,len(a)):

   n+=a[i]

   n+=b[i]

 print(n)
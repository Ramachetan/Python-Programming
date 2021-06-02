'''
Write a program that generates 100 random integers that are either 0 or 1.
Then find the longest run of zeros, the largest number of zeros in a row.
For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
'''
import random
x=[]
for i in range(100):
    x.append(random.randint(0,1))
maxzero=0
count=0
for i in range(len(x)):
    if(x[i]==0):
        count=count+1
        
        if(i==len(x)-1):
            if(count>maxzero):
                maxzero=count         
    if(x[i]==1):
        if(count>maxzero):
            maxzero=count
        count=0
print("Longest run of Zeros in a row is",maxzero)
    

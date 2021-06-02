'''
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.

'''
import random
l=[]
for i in range(20):
    l.append(random.randint(1,100))
print("List: ",l)
print("Average: ", round(sum(l)/len(l),2))
print("Largest Value in List: ",max(l))
print("Smallest Value in List: ",min(l))
l1=sorted(l)
print("Second Largest Value in List: ",l1[-2])
print("Smallest Value in List: ",l1[1])
count=0
for i in l:
    if i%2==0:
        count+=1
print("Number of Even Numbers in the list: ",count)


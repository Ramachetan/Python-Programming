'''
Write a function called merge that takes two already sorted lists of
possibly different lengths, and merges them into a single sorted list.
(a) Do this using the sort method.
(b) Do this without using the sort method.
'''
def merge(l1,l2):
    s1=len(l1)
    s2=len(l2)
    l=[]
    i,j=0,0
    while i<s1 and j<s2:
        if l1[i]<l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    return (l+l1[i:]+l2[j:])
a=list(map(int,input("Enter sotred list 1: ").split()))
b=list(map(int,input("Enter sotred list 2: ").split()))
print("sorted list after merging:",merge(a,b))

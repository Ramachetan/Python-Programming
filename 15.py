'''
Write a program that removes any repeated items from a list so that each
item appears at most once. For instance, the list [1,1,2,3,4,3,0,0]
would become [1,2,3,4,0].
'''
l=list(map(int,input("Enter the elements into list with duplication: ").split(',')))
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)





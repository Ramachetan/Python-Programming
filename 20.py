'''
Write a function called is_sorted that is given a list and returns
True if the list is sorted and False otherwise.
'''
def is_sorted(l):
    x=l[:]
    x.sort()
    if l==x:
        return True
    else:
        return False
l=list(input("Enter list items : ").split())
print(is_sorted(l))

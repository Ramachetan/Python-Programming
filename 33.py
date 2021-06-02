'''
Write a program to demonstrate Try/except/else.
'''
try:
    a=int(input("Enter 'a' value: "))
    b=int(input("Enter 'b' value: "))
    c=a//b
except ZeroDivisionError:
    print("Division can't possible (b=0)")
else:
    print(" a//b Value:",c)

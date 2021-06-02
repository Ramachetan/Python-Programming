'''
Write a function called root that is given a number x and an integer n and
returns x1/n. In the function definition, set the default value of n to 2.
'''
def root(x,n=2):
    return (x**(1/n))
x=int(input("Enter 'x' value: "))
n=int(input("Enter 'n' value: "))
ans1=root(x,n)
ans2=root(x)
print("Root value with n value: ",ans1)
print("Root Value with out n value (Default 2): ",ans2)



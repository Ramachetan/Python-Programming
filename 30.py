'''
Write a Python class to implement pow(x, n)
'''
class power:
    def pow(self,x,n):
        print("pow(",x,",",n,") =",x**n)
p=power()
x=int(input("Enter 'x' value : "))
n=int(input("Enter 'n' value : "))
p.pow(x,n)

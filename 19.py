'''
Write a function called number_of_factors that takes an integer and
returns how many factors the number has.
'''
def number_of_factors(n):
    fact_count=0
    for i in range(1,n+1):
        if(n%i==0):
            fact_count+=1
    return fact_count
n=int(input("Enter an integer: "))
x=number_of_factors(n)
print("factors count is",x)
   

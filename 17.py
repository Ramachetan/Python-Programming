'''
Write a function called sum_digits that is given an integer num and
returns the sum of the digits of num.
'''
def sum_digits(num):
    sum=0
    while(num>0):
        sum=sum+num%10
        num=num//10
    return sum
x=int(input("Enter a number: "))
s=sum_digits(x)
print("Sum of digits: ",s)

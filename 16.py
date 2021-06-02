'''
Write a program that asks the user to enter a length in feet.
The program should then give the user the option to convert from feet
into inches, yards, miles, millimeters, centimeters, meters, or kilometers.
Say if the user enters a 1, then the program converts to inches,
if they enter a 2, then the program converts to yards, etc.
While this can be done with if statements,it is much shorter with lists and
it is also easier to add new conversions if you use lists.
'''
feet=int(input("Enter feet: "))
opt=int(input("enter  choice 1:inches   2:yards   3:miles   4:millimeters   5:centimeters   6:meters  7:kilometers --->"))
l=[round(feet*12,3),round(feet*0.333,3),round(feet*0.000189,3),round(feet*304.8,3),\
   round(feet*30.48,3),round(feet*0.305,3),round(feet*0.000305,3)]
print(l[opt-1])



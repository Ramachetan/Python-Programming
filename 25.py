'''
Write a program that reads a file consisting of email addresses,
each on its own line.
Your program should print out a string consisting of those email addresses
separated by semicolons.
'''

file=open(input("Enter file name: "),'r')
Lines=file.readlines()
for line in range(len(Lines)):
   if(line==len(Lines)-1):
      print('{}'.format(Lines[line].strip()))
   else:
       print('{}'.format(Lines[line].strip()),end=";")

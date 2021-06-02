'''
with statement in Python is used in exception handling to make the code cleaner and much more readable.
It simplifies the management of common resources like file streams.

Write a program to demonstrate try/finally and with/as

'''

file = open('file1.txt', 'w') 
try: 
    file.write('hello friends how are you') 
finally: 
    file.close()
    
with open('file2.txt', 'w') as file: 
    file.write('hello friends how are you') 

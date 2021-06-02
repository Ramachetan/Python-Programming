'''
Write a program that reads a list of temperatures from a file called temps.txt,
converts those temperatures to Fahrenheit, and writes the results to a file
called ftemps.txt.
'''
file1 = open('temps.txt', 'r') 
lines = file1.readlines()
file2 = open('ftemps.txt', 'w')
for i in range(len(lines)):
    c=lines[i].strip()
    f=round((float(c)*1.8)+32,2)
    file2.write(str(f)+"\n")
file2.close() 

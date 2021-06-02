'''
Write a program that opens a file dialog that allows you to select a text file.
The program then displays the contents of the file in a textbox.
'''
from tkinter import filedialog
from tkinter import Tk
from tkinter import *
root = Tk()
root.fileName = filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All Files","*.*")))
text1 = open(root.fileName).read()
T = Text(root, height=25, width=80)
T.pack()                   
T.insert(END,text1) #END (or “end”) corresponds to the position just after the last character in the buffer.
root.mainloop()

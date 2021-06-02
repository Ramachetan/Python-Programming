'''
Write a program that asks the user for a word and finds all the
smaller words that can be made from the letters of that word.
The number of occurrences of a letter in a smaller word can’t
exceed the number of occurrences of the letter in the user’s word.
'''

from itertools import permutations
s=input("Enter a word: ")
for i in range(2,len(s)):
   for p in permutations(s,i):
       print(''.join(p),end=' ')

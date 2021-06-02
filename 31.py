'''
Write a Python class to reverse a string word by word.
'''
class reverse:
   def rev_sentence(self,sentence):
      words = sentence.split(' ')
      reverse_sentence = ' '.join(reversed(words))  
      print(reverse_sentence)  
c=reverse()
c.rev_sentence(input("Enter the string: "))

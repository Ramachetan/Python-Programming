def printVowels(string):
    for char in string:
        if char in "aeiouAEIOU":
            print("Vowel->",char, end=', ')
        else:
            print("Not a Vowel=>",char, end=', ')

    return char

string = input('Enter any string: ')

printVowels(string)
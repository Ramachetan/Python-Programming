import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 '))
    if target_num != guess_num:{
    print("Try Again")}

print('Well guessed!')
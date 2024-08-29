
import random
# list_of_words = ['Ronaldo', 'Messi', 'Mbappe']


# my_choice = input('Your player please? ')
# your_choice = random.choice(list_of_words)

# if your_choice == my_choice:
#     print('LA28 Olympics passes!')
# else:
#     print('Try again!')


list_of_words = ['t', 'o', 'w', 'e', 'r']
hangman = ""
count = 0
max_attempts = 3
while count <= 3:
    machine_choice = random.choice(list_of_words)
    your_choice = input('What is your word? ')

    if your_choice == machine_choice:
        hangman += your_choice
        print('Correct guess, so far the word is:', hangman)
    else:
        count += 1
        print('Incorrect guess, attempts left :', max_attempts - count)
    if len(hangman) == len(list_of_words):
        print("Guessed it right!")
        break;
if count > max_attempts:
    print("Game over!")








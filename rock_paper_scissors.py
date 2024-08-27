import random

rock = r"""
        _______
    ----'   ____)
          (_____)
          (_____)
          (____)
    ----.__(___)
    """


paper = r"""
         _______
    ----'    ____)____
               ______)
              _______)
             _______)
    ----.__________)
    """


scissors = r"""
        _______
    ----'   ____)____
              ______)
           __________)
          (____)
    ----.__(___)
    """


game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))
#0-- rock, 1-- paper, 2-- scissors
print(game_images[user_choice])
machine_choice = random.randint(0,2)
print(game_images[machine_choice])

if user_choice >= 3 or user_choice < 0:
    print('Invalid number, User lose!')
elif user_choice == 0 and machine_choice == 2:
    print('User wins')
elif machine_choice == 0 and user_choice == 2:
    print('Machine wins')
elif machine_choice > user_choice:
    print('Machine wins')
elif user_choice > machine_choice:
    print('User wins')
elif user_choice == machine_choice :
    print("It's a draw")
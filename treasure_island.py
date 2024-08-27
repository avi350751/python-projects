#Project - Treasure Island

print("Welcome to Treasure island !\nYour mission is to find the treasure")
print("""
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 \n""")

which_way = input("You're  at a cross road . Where do you want to go? Type 'left' or 'right' ")
if which_way.lower() == 'left':
    swim_wait = input("You've come to a lake. There is an island in the middle of a lake.\nType 'wait' to wait for a boat.\nType 'swim' to swim across ")
    if swim_wait.lower() == 'wait':
        choice = input("Which door you choose? red, yellow or green: ").lower()
        if choice == 'red':
            print("It's a room full of fire. Game Over!")
        elif choice == 'yellow':
            print("You found the treasure. You Win!!")
        elif choice == 'green':
            print("You enter a room of beasts. Game Over!!")
    else:
        print('game Over!')    
else:
    print('Game Over!')
    
#Set initial play variable to yes
play = "y"

#Set initial starting number to zero
start = 0

#If user wants to continue play
while play == "y":

    #Request the user's choice
    user_choice = int(input("How many numbers would you like? "))
        
    #For loop
    for start in range(start, start + user_choice):
        print(start)
    start = start + 1
    play = input("Would you like to continue? (Y/N)" )

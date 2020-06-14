#Set initial play variable to yes
play = "y"

#If user wants to continue play
while play == "y":

    #Request the user's choice
    user_choice = int(input("How many numbers would you like? "))
    
    #Reset index to zero
    i = 0
    
    #Run loop
    while i < user_choice:
        print(i)
        i = i + 1
    
    play = input("Would you like to continue? (Y/N)" )

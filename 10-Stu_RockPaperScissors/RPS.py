# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == "r" and computer_choice == "r"):
    print("You chose rock. Hal chose rock.")
    print("You tied!")
elif (user_choice == "r" and computer_choice == "p"):
    print("You chose rock. Hal chose paper.")
    print("Dismal choice, Hal had it wrapped around you on this one!")
elif (user_choice == "r" and computer_choice == "s"):
    print("You chose rock. Hal chose scissors.")
    print("Great choice, you crushed Hal!")
elif (user_choice == "p" and computer_choice == "r"):
    print("You chose paper. Hal chose rock.")
    print("Great choice, you had it wrapped around Hal on this one.")
elif (user_choice == "p" and computer_choice == "p"):
    print("You chose paper. Hal chose paper.")
    print("You tied!")
elif (user_choice == "p" and computer_choice == "s"):
    print("You chose paper. Hal chose scissors.")
    print("Dismal choice, Hal cut you to pieces on this one!")
elif (user_choice == "s" and computer_choice == "r"):
    print("You chose scissors. Hal chose rock.")
    print("Dismal choice, Hal crushed you!")
elif (user_choice == "s" and computer_choice == "p"):
    print("You chose scissors. Hal chose paper.")
    print("Great choice, you cut Hal to pieces on this one!")
elif (user_choice == "s" and computer_choice == "s"):
    print("You chose scissors. Hal chose scissors.")
    print("You tied!")
else:
    print("Invalid input.")
    print("Next time try r, p or s.")



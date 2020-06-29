lottery_numbers = {13, 21, 22, 5, 8}
"""
A player looks like this:
{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}
Define a list with two players (you can come up with their names and numbers).
"""
players = [{
    'name': 'Benjamin',
    'numbers': {28, 5, 7, 22, 3}
},
{
    'name': 'Sally',
    'numbers': {8, 11, 2, 7, 13}
}]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
#lucky_numbers = players[name].intersection(lottery_numbers)
#how_many_numbers = len(lucky_numbers)
#print("Player " + players[name] + " got " + str(how_many_numbers) + " numbers right.")

#Check Lesson 23 for solution

name = players[0]["name"]
how_many_numbers = len(players[0]["numbers"].intersection(lottery_numbers))
print("Player " + name + " got " + str(how_many_numbers) + " numbers right.")

name = players[1]["name"]
how_many_numbers = len(players[1]["numbers"].intersection(lottery_numbers))
print("Player " + name + " got " + str(how_many_numbers) + " numbers right.")

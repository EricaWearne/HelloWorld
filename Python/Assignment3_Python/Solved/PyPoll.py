#Import required modules
import os
import csv

#Path to csv data file
PyPoll_file_path = os.path.join("..", "Resources", "election_data.csv")

#Declaring global variables
vote_total = ()
candidates = []
unique_candidate = []
candidate_votes = []
candidate_votes_percentage = []

#Open input csv and read columns of interest into our lists
with open(PyPoll_file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    #finding total number of votes
    rows = list(csvreader)
    vote_total = len(rows)

    #determining unique candidates and votes
    for row in csvreader:
        candidates.append(rows[2])
        unique_candidate.append(rows)
        x = candidates.count(row)
        candidate_votes.append(x)

    #determining vote percentage
        y = (x/vote_total)*100
        candidate_votes_percentage.append(y)

max_vote_count = max(candidate_votes)
winner = unique_candidate[candidate_votes.index(max_vote_count)]
            
print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_total}")
print("----------------------------")
print(f"{unique_candidate[0]}: ")
print(f"{unique_candidate[1]}: ")
print(f"{unique_candidate[2]}: ")
print(f"{unique_candidate[3]}: ")
print("----------------------------")
print("Winner: ") #print winner
print("----------------------------")


with open("PyPoll.txt", "w", newline='') as final_csvfile:
    final_csvfile.write("Election Results\n")
    final_csvfile.write("----------------------------\n")
    final_csvfile.write(f"Total Votes: {vote_total}\n")
    final_csvfile.write("----------------------------\n")

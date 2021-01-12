import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('analysis', 'pypoll.txt')

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
winner = ""
candidates = ['Khan', 'Correy', 'Li', 'OTooley']
highest_votes = 0
votes = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            OTooley_votes += 1


dict_votes_per_candidate = {
    "Khan": Khan_votes,
    "Correy": Correy_votes,
    "Li": Li_votes,
    "O'Tooley": OTooley_votes
}

for candidate, votes in dict_votes_per_candidate.items():
    if votes > highest_votes:
        highest_votes = votes
        winner = candidate


output = f"""
Election Results
---------------------
Total Votes: {total_votes}
---------------------
Khan: {(Khan_votes/total_votes)*100:.3f}%, ({Khan_votes})
Correy: {(Correy_votes/total_votes)*100:.3f}%, ({Correy_votes})
Li: {(Li_votes/total_votes)*100:.3f}%, ({Li_votes})
O'Tooley: {(OTooley_votes/total_votes)*100:.3f}%, ({OTooley_votes})
---------------------
Winner: {winner}
---------------------
"""
print(output)

with open(output_file, 'w') as updated_output_file:
    updated_output_file.write(output)

#Citation:
#Title: Poll_main source code 
# Author: Chao, D.
# Date: 2021
# Code version: 1.0
# Availability: Used as reference in tutoring session  
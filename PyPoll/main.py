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

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_votes += 1

      




output = f"""
Election Results
---------------------
Total Votes: {total_votes}
---------------------
Khan: %, (total votes)
Correy: %, (total votes)
Li: %, (total votes)
O'Tooley: %, (total votes)
---------------------
Winner:
---------------------
"""
print(output)

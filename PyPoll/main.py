import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('analysis', 'pypoll.txt')


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")




output = f"""
Election Results
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

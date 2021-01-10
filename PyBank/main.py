import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('analysis', 'pybank.txt')

total_months = 0
net_total = 0
previous_budget = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
       print(row)




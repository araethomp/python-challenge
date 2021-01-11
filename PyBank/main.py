import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('analysis', 'pybank.txt')

total_months = 0
net_total = 0
budget = 0
previous_budget = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""
total_change = 0
change = 0
change_count = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_months += 1 
        print(row)
        
        budget = int(row[1])
        net_total += budget

    



output = f"""
Financial Analysis 
--------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: 
Greatest Increase in Profits:
Greatest Decrease in Profits:
"""
print(output)

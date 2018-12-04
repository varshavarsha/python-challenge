
import os
import csv

budget_csv = os.path.join('.', 'budget_data.csv')

total_months = 0
profit_losses = 0
#profit_counter = 867884
#losses_counter = 867884


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:
        profit_counter = int(row[1])
        losses_counter = int(row[1])
        break
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        profit_losses += int(row[1])
        if int(row[1]) > profit_counter:
            profit_counter = int(row[1])
            profit_month = row[0]

        if int(row[1]) < losses_counter:
            losses_counter = int(row[1])
            losses_month = row[0]

    average_change = profit_losses / total_months
    print("Financial Analysis")
    print("-------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Average Change: {'${:,.2f}'.format(average_change)}")
    print(f"Greatest Increase in Profits: {profit_month} ({'${:,.2f}'.format(profit_counter)})")
    print(f"Greatest Decrease in Profits: {losses_month} ({'${:,.2f}'.format(losses_counter)})")


file = open("output_file.txt", "w")
file.write("Financial Analysis\n")
file.write("-------------------------------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Average Change: {'${:,.2f}'.format(average_change)}\n")
file.write(f"Greatest Increase in Profits: {profit_month} ({'${:,.2f}'.format(profit_counter)})\n")
file.write(f"Greatest Decrease in Profits: {losses_month} ({'${:,.2f}'.format(losses_counter)})\n")
file.close()






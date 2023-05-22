import csv

budget_data = r"C:\Users\Mason\python-challenge\PyBank\Resources\budget_data.csv"
text = r"C:\Users\Mason\python-challenge\PyBank\analysis\analysis.txt"

months = 0
net = 0
previous = 0
total = 0
average = 0
increase = ["", 0]
decrease = ["", 0]

with open(budget_data) as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    for row in data:
        months += 1
        date = row[0]
        profit_losses = int(row[1])
        net += profit_losses
        change = profit_losses - previous
        total += change
        previous = profit_losses
        if change > increase[1]:
            increase = [date, change]
        if change < decrease[1]:
            decrease = [date, change]

average = total / (months - 1)

output = "Financial Analysis\n"
output += "----------------------------\n"
output += f"Total Months: {months}\n"
output += f"Net Total Profit/Losses: ${net}\n"
output += f"Average Change: ${average:.2f}\n"
output += f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
output += f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n"

with open(text, "w") as Analysis:
    Analysis.write(output)

total_months = 0
net_total_profit_losses = 0
prev_profit_losses = 0
total_changes = 0
avg_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)
    for row in csvreader:
        # Update total number of months
        total_months += 1
        # Extract date and profit/losses from the row
        date = row[0]
        profit_losses = int(row[1])
        # Update net total profit/losses
        net_total_profit_losses += profit_losses
        # Calculate change in profit/losses
        change = profit_losses - prev_profit_losses
        # Update total changes
        total_changes += change
        # Update previous profit/losses for the next iteration
        prev_profit_losses = profit_losses
        # Check for greatest increase in profits
        if change > greatest_increase[1]:
            greatest_increase = [date, change]
        # Check for greatest decrease in profits
        if change < greatest_decrease[1]:
            greatest_decrease = [date, change]

# Calculate average change
avg_change = total_changes / (total_months - 1)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Profit/Losses: ${net_total_profit_losses}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
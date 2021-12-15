# Import dependencies
import os, csv

# State file location
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Create lists to iterate through
dates = []
profit_loss = []
monthly_change = []

# Initialize any variables
total_profit = 0

# Open csv file using path budget_csv
with open(budget_csv) as csvfile:
    # Translate csv file and set delimiter to navigate to different column
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip headers to iterate only values
    header = next(csvreader)

    # Iterate through the rows
    for row in csvreader:
        # Append dates and profit_loss information to their lists
        dates.append(row[0])
        profit_loss.append(row[1])
        # Calculate total_profit
        total_profit = total_profit + int(row[1])

    # Iterate through profit_loss to get monthly change in profits
    for i in range(1, len(profit_loss)):
        # Take the difference between two months and append to monthly_change
        monthly_change.append(int(profit_loss[i]) - int(profit_loss[i-1]))

# Retrieve the max and min of the monthly_change list
greatest_inc_profit = max(monthly_change)
greatest_dec_profit = min(monthly_change)
# Tie in max and min to correct month using month list. Index from max and min
# Utilize + 1 since the month correlated to change is the next month
greatest_inc_month = monthly_change.index(max(monthly_change)) + 1
greatest_dec_month = monthly_change.index(min(monthly_change)) + 1 

# Print Statements
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(dates)}')
print(f'Total: ${total_profit}')
print(f'Average Change: {round(sum(monthly_change) / len(monthly_change), 2)}')
print(f'Greatest Increase in Profits: {dates[greatest_inc_month]} (${(str(greatest_inc_profit))})')
print(f'Greatest Decrease in Profits: {dates[greatest_dec_month]} (${(str(greatest_dec_profit))})')

# Output file
analysis = os.path.join('analysis', 'analysis.txt')

# Export to .txt file
with open(analysis, 'w') as text:
    text.write('Financial Analysis' + '\n')
    text.write('----------------------------' + '\n')
    text.write(f'Total Months: {len(dates)}' + '\n')
    text.write(f'Total: ${total_profit}' + '\n')
    text.write(f'Average Change: {round(sum(monthly_change) / len(monthly_change), 2)}' + '\n')
    text.write(f'Greatest Increase in Profits: {dates[greatest_inc_month]} (${(str(greatest_inc_profit))})' + '\n')
    text.write(f'Greatest Decrease in Profits: {dates[greatest_dec_month]} (${(str(greatest_dec_profit))})' + '\n')


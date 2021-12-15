# Import dependencies
import os, csv

# State file location
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Create lists to iterate through
candidate = []
vote_num = []
vote_percent = []

# Initialize any variables
total_votes = 0

# Open csv file using path election_data_csv and create new line after empty space
with open(election_data_csv) as csvfile:
    # Translate csv file and set delimiter to navigate to different column
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip headers to iterate only values
    csv_header = next(csvreader)

    # Iterate through the rows
    for row in csvreader:
        total_votes += 1

        #If the candidate is not on the list, we will add their name and a vote
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            vote_num.append(1)
        #Else, if the candidate is on the list, we will add a vote to their name
        else:
            index = candidate.index(row[2])
            vote_num[index] += 1

    # Add to percent_votes list 
    for votes in vote_num:
        # Percentage total
        percentage = (votes / total_votes) * 100
        # Round percentage total
        percentage = round(percentage)
        # Add 3 decimal points
        percentage = "%.3f%%" % percentage
        # Append vote_percent list to percentages
        vote_percent.append(percentage)

    # Find the winning candidate
    winner = max(vote_num)
    # Index vote_num to winner
    index = vote_num.index(winner)
    # Find name of winner
    winning_candidate = candidate[index]

# Print Statements
print('Election Results')
print('--------------------------')
print(f'Total Votes: {str(total_votes)}')
print('--------------------------')
for i in range(len(candidate)):
    print(f'{candidate[i]}: {str(vote_percent[i])} ({str(vote_num[i])})')
print('--------------------------')
print(f'Winner: {winning_candidate}')
print('--------------------------')

# Output file
analysis = os.path.join('analysis', 'analysis.txt')

# Export to .txt file
with open(analysis, 'w') as text:
    text.write('Election Results' + '\n')
    text.write('--------------------------' + '\n')
    text.write(f'Total Votes: {str(total_votes)}' + '\n')
    text.write('--------------------------' + '\n')
    for i in range(len(candidate)):
        text.write(f'{candidate[i]}: {str(vote_percent[i])} ({str(vote_num[i])})' + '\n')
    text.write('--------------------------' + '\n')
    text.write(f'Winner: {winning_candidate}' + '\n')
    text.write('--------------------------' + '\n')
import csv

#Declare Variable
total_votes = 0
list_candidates = []
list_ballots = []
list_counties = []
vote_won = 0
input_file = r'resources\election_data.csv'
output_file = r'analysis\PyPoll_FinalResults.txt'

#import csv
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader)

    for row in csvreader:
        candidate = row[2]
        ballot = row[2]
        county = row[1]

        total_votes += 1
        #List of all votes with candidates
        list_ballots.append(ballot)

        #Collect a list of candidates
        if candidate not in list_candidates:
            list_candidates.append(candidate)
            list_counties.append(county)

#Print results in terminal
print('Election Results\n')
print('-------------------------\n')
print(f'Total Vote: {total_votes}\n')
print('-------------------------\n')

#Loop to make the results dynamic
for candidate in list_candidates:
    #Calculate the total votes & %
    print(f'{candidate}: {round(list_ballots.count(candidate)/total_votes*100,3)}% ({list_ballots.count(candidate)})\n')
    #Finding the winner
    if list_ballots.count(candidate) > vote_won:
        vote_won = list_ballots.count(candidate)
        winner = candidate
print('-------------------------\n')
print(f'Winner: {winner}\n')
print('-------------------------\n')


#Create a textfile
with open(output_file, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Vote: {total_votes}\n')
    txtfile.write('-------------------------\n')
    for candidate in list_candidates:
        #Calculate the total votes & %
        txtfile.write(f'{candidate}: {round(list_ballots.count(candidate)/total_votes*100,3)}% ({list_ballots.count(candidate)})\n')
        #Finding the winner
        if list_ballots.count(candidate) > vote_won:
            vote_won = list_ballots.count(candidate)
            winner = candidate
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('-------------------------\n')

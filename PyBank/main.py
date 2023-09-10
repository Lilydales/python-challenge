import csv

# assign Variable
total_month = 0
net_total = 0
previous_profit_loss = 0
monthly_changes = []
dates = []
input_file = r'resources\budget_data.csv'
output_file = r'analysis\PyBank_FinalResults.txt'

# import csv file
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# skip header row
    next(csvreader)

    for row in csvreader:
    #Retrieve the date & profit/loss values
        date = row[0]
        profit_loss = int(row[1])

        #Calculate the total num of months
        total_month += 1

        #Calculate the change in profit/loss from pre months
        if total_month > 1:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            dates.append(date)

        previous_profit_loss = profit_loss

#Calculate the average change in profit/loss
average_change = round(sum(monthly_changes) / len(monthly_changes), 2)

#Find the max increase and decrease in profit
max_increase = max(monthly_changes)
max_decrease = min(monthly_changes)

#Match the date for the above value
max_increase_date = dates[monthly_changes.index(max_increase)]
max_decrease_date = dates[monthly_changes.index(max_decrease)]

#Save results to textfile
with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: ${total_month}\n")
    txtfile.write(f"Total : ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profit: {max_increase_date} (${max_increase})\n")
    txtfile.write(f"Greatest Decrease in Profit: {max_decrease_date} (${max_decrease})\n")

#Print the above results in Terminal
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: ${total_month}\n")
print(f"Total : ${net_total}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profit: {max_increase_date} (${max_increase})\n")
print(f"Greatest Decrease in Profit: {max_decrease_date} (${max_decrease})\n")
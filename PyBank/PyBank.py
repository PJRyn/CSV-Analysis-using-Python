#Importing os to locate budget_data.csv and Analysis_output.txt. Csv reads csv filesS
import os
import csv

#locates budget_data.csv
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Initializes variables used in code
month_count = 0
budget_total = 0
biggest_loss = 0
pre_profloss = 0
biggest_change = 0
changes = []

#Open and read budget_data_csv without reading the header
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #Counts months, objective 1
        month_count += 1

        #counts and calculates the total of the profits and losses, objective 2
        profit_and_loss = float(row[1])
        budget_total = budget_total + profit_and_loss
        
        #find the change in profits from previous entry to current entry, adds that to a list of changes in profit objective 3
        change_in_profit_and_loss = profit_and_loss - pre_profloss
        changes = changes + [change_in_profit_and_loss]

        #from the change in profit and loss it looks for the biggest and smallest then takes thier dates, objective 4 & 5
        if change_in_profit_and_loss > 0 and change_in_profit_and_loss>biggest_change:
            biggest_change = change_in_profit_and_loss
            prof_date = str(row[0])
        elif change_in_profit_and_loss < 0 and change_in_profit_and_loss<biggest_loss:
            biggest_loss = change_in_profit_and_loss
            loss_date = str(row[0])
        
        #makes the current profit_and_loss into previous profit and loss for next interation through the .csv
        pre_profloss = profit_and_loss
    
    #find the average change in profit and loss, objective 3
    average_change = round(sum(changes)/len(changes),2)

#load output path
output_path = os.path.join("Analysis", "Analysis_output.txt")

#outputs the analysis
with open(output_path, 'w') as text:
    text.writelines(['Financial Analysis'
                    f'\n----------------------------'
                    f'\nTotal Months: {str(month_count)}'
                    f'\nTotal: ${str(int(budget_total))}'
                    f'\nAverage Change: ${str(average_change)}'
                    f'\nGreatest Increase in Profits: {prof_date} (${str(int(biggest_change))})'
                    f'\nGreatest Decrease in Profits: {loss_date} (${str(int(biggest_loss))})'])
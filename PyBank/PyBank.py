import os
import csv
budget_data_csv = os.path.join("Resources", "budget_data.csv")
print(budget_data_csv)
month_count = 0
budget_total = 0
biggest_loss = 0
change = 0
pre_profloss = 0
biggest_change = 0
changes = []
with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        month_count += 1
        profloss = float(row[1])
        budget_total = budget_total + profloss
        change = profloss - pre_profloss
        changes = changes + [change]
        if change > 0 and change>biggest_change:
            print('')
            biggest_change = change
            prof_date = str(row[0])
        elif profloss < 0 and change<biggest_loss:
            print('')
            biggest_loss = change
            loss_date = str(row[0])
        pre_profloss = profloss
    average_change = round(sum(changes)/len(changes),2)
output_path = os.path.join("Analysis", "Analysis_output.csv")
with open(output_path, 'w') as text:
    text.writelines('Financial Analysis')
    text.writelines(f'\n----------------------------')
    text.writelines(f'\nTotal Months: {str(month_count)}')
    text.writelines(f'\nTotal: ${str(int(budget_total))}')
    text.writelines(f'\nAverage Change: ${str(average_change)}')
    text.writelines(f'\nGreatest Increase in Profits: {prof_date} (${str(int(max(changes)))})')
    text.writelines(f'\nGreatest Decrease in Profits: {loss_date} (${str(int(min(changes)))})')
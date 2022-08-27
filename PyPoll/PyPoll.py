#Importing os to locate budget_data.csv and Analysis_output.txt. Csv reads csv filesS
import os
import csv

#initalize variables
vote_count_total = 0
ccs_vote_count = 0
dd_vote_count = 0
rad_vote_count = 0

#locates budget_data.csv
budget_data_csv = os.path.join("Resources", "election_data.csv")

#Open and read budget_data_csv without reading the header
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        
        #total vote count
        vote_count_total += 1
        
        #find the total votes for each candiate
        candidate = row[2]
        if candidate == "Charles Casper Stockham":
            ccs_vote_count += 1
        elif candidate == "Diana DeGette":
            dd_vote_count += 1
        elif candidate == "Raymon Anthony Doane":
            rad_vote_count += 1
    
    #find the percentage of votes for each candidate
    ccs_vote_percent = round(ccs_vote_count/vote_count_total * 100, 3)
    dd_vote_percent = round(dd_vote_count/vote_count_total * 100, 3)
    rad_vote_percent = round(rad_vote_count/vote_count_total * 100, 3)
    
    #created a dictionary to quickly find the winner of the election
    candidate_and_votes = {
        "Charles Casper Stockham": ccs_vote_count,
        "Diana DeGette": dd_vote_count, 
        "Diana DeGette": rad_vote_count
        }

#load output path
output_path = os.path.join("Analysis", "Analysis_output.txt")

#outputs the analysis
with open(output_path, 'w') as text:
    text.write("Election Results")
    text.write(f"\n-------------------------")
    text.write(f"\nTotal Votes: {vote_count_total}")
    text.write(f"\n-------------------------")
    text.write(f"\nCharles Casper Stockham: {ccs_vote_percent}% ({ccs_vote_count})")
    text.write(f"\nDiana DeGette: {dd_vote_percent}% ({dd_vote_count})")
    text.write(f"\nRaymon Anthony Doane: {rad_vote_percent}% ({rad_vote_count})")
    text.write(f"\n-------------------------")
    text.write(f"\nWinner: {max(candidate_and_votes)}")
    text.write(f"\n-------------------------")


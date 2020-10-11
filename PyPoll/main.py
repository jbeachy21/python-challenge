import os
import csv


election_csv = os.path.join('Resources', 'election_data.csv')


with open(election_csv, 'r') as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    TotalVotes = 0
    winner = ""
    collection = {}
    khan = 0
    correy = 0
    li = 0
    tooley = 0
    for row in csvreader:
       
        
        TotalVotes+= 1

        if row[2] == "Khan":
            khan+=1
            collection[row[2]] = khan
        elif row[2] =="Correy":
            correy+=1
            collection[row[2]] = correy
        elif row[2] == "Li":
            li+=1
            collection[row[2]] = li
        else:
            tooley+=1
            collection[row[2]] = tooley
        
       
        
    khanpercent = (khan/TotalVotes) * 100
    correypercent = (correy/TotalVotes) * 100
    lipercent = (li/TotalVotes) * 100
    tooleypercent = (tooley/TotalVotes) * 100
    
        
    print(collection.items())
    

    print("Election Results")
    print("-------------------------")
    print(f"Total votes: {TotalVotes}")
    print("-------------------------")
    print(f"Khan: {khanpercent}%  and {khan} votes")
    print(f"Correy: {correypercent}%  and {correy} votes")
    print(f"Li: {lipercent}%  and {li} votes")
    print(f"O'Tooley: {tooleypercent}%  and {tooley} votes")
    print("-------------------------")
    print("Winner: ")




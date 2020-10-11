import os
import csv
import math

election_csv = os.path.join('Resources', 'election_data.csv')


with open(election_csv, 'r') as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    TotalVotes = 0
    


    # Dictionary to keep track of candidates and total votes (candidate, total votes)
    collection = {}
    # counter variables to make tracking votes easier
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
    


    # makes a list of the keys (total votes of each candidate)
    values = collection.values()
    keys = collection.keys()
    # getting max from collection of voting data
    x = max(values)
    
    winner = ""
    for i in keys:
        # print(i)
        if collection.get(i) == x:
            winner = i
        
    # print(collection.items())
    

    print("Election Results")
    print("-------------------------")
    print(f"Total votes: {TotalVotes}")
    print("-------------------------")
    print(f"Khan: {math.ceil(khanpercent)}%  and {khan} votes")
    print(f"Correy: {math.ceil(correypercent)}%  and {correy} votes")
    print(f"Li: {math.ceil(lipercent)}%  and {li} votes")
    print(f"O'Tooley: {math.ceil(tooleypercent)}%  and {tooley} votes")
    print("-------------------------")
    print(f"Winner: {winner}")




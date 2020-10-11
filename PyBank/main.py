import os
import csv


budget_csv = os.path.join('Resources', 'budget_data.csv')


with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    header = next(csvreader)
    # variable for number of months
    i = 0
    # netprofit variable
    netprofit = 0
    #greatest incrase and decrease variables 
    GreatestIncrease = 0
    GreatestDecrease = 0
    current = 0
    previous = 0
    AverageChange = 0
    for row in csvreader:
        previous = current
        current = row[1]
        Delta = int(current) - int(previous)
        netprofit= netprofit + int(row[1])
        print(row[1])
        
        i+=1
        
        if Delta > GreatestIncrease:
            GreatestIncrease = Delta
            AverageChange+= GreatestIncrease
        if Delta < 0 and Delta < GreatestDecrease:
            GreatestDecrease = Delta
            AverageChange+= GreatestDecrease
            
        
    

    # AverageChange/= (GreatestDecrease + GreatestIncrease)
    AverageChange = AverageChange/i
    print(f"Total months: {i}")
    print(f"Net Profit: {int(netprofit)}")
    print(f"Average Change: {int(AverageChange)}")

    print(f"Greatest increase: {GreatestIncrease}")
    print(f"Greatest decrease: {GreatestDecrease}")
       


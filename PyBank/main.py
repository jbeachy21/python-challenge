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
    netChangeList = []
    for row in csvreader:
        previous = current
        current = row[1]
        Delta = int(current) - int(previous)
        netprofit= netprofit + int(row[1])

        netChangeList.append(Delta)
     
        i+=1
        
        if Delta > GreatestIncrease:
            GreatestIncrease = Delta
            
        if Delta < 0 and Delta < GreatestDecrease:
            GreatestDecrease = Delta
            
    
    AverageChange = sum(netChangeList)/len(netChangeList)
    print("Financial Analysis:")
    print("-------------------------")
    print(f"Total months: {i}")
    print(f"Net Profit: {int(netprofit)}")
    print(f"Average Change: {int(AverageChange)}")

    print(f"Greatest increase: {GreatestIncrease}")
    print(f"Greatest decrease: {GreatestDecrease}")





    file = open("./Analysis/analysis.txt", "w+")

    file.write("Financial Analysis:")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total months: {i}")
    file.write("\n")
    file.write(f"Net Profit: {int(netprofit)}")
    file.write("\n")
    file.write(f"Average Change: {int(AverageChange)}")
    file.write("\n")
    file.write(f"Greatest increase: {GreatestIncrease}")
    file.write("\n")
    file.write(f"Greatest decrease: {GreatestDecrease}")


    file.close()
       


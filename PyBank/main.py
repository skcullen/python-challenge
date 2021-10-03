# import needed modules
import os
import csv

#create empty lists to store the data
months = []
profits = []
profitchange = []

#create path to needed data file
csvpath = os.path.join('Resources','budget_data.csv')

#set up to read csv file, skipping the header
with open(csvpath, 'r') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=',')
    csv_header = next(csvreader)

    #set up code to loop through rows
    for column in csvreader:

        #fill in lists with column data, will ultimately use this to calclate sum and change in lists
        months.append(column[0])
        profits.append(int(column[1]))

    #set up another loop to calculate the change for each row of profit
    for x in range(len(profits)-1):

        #calculate the change month to month
        profitchange.append(profits[x+1]-profits[x])


    #calculate average change
    averagechange = sum(profitchange) / len(profitchange) 

    #calculate min and max of profitchange
    maxchange = max(profitchange)
    minchange = min(profitchange)

    #get the correlating month for the min and max
    for x in range(len(profits)-1):
        if profits[x+1] - profits[x] == maxchange:
            maxmonth = months[x+1]
        elif profits[x+1] - profits[x] == minchange:
            minmonth = months[x+1]





#create output data
print("Financial Analysis")
print("--------------------------------------")

#get total number of months using the length function
print(f"Total Months: {len(months)}")

#total profit using sum of the profit list
print(f"Total: ${sum(profits)}")

#find average using list profit change
print(f"Average Change: ${averagechange:.2f}")

#greatest increase and decrease
print(f"Greatest Increase in Profits: {maxmonth} (${maxchange})")
print(f"Greatest Decrease in Profits: {minmonth} (${minchange})")

#export the results into a txt file
#write the path for where we want the results
output = os.path.join("analysis", "budget_summary.txt")

#open file in write mode and fill in the output data
with open(output, 'w') as f:
    f.write("Financial Analysis" '\n')
    f.write("--------------------------------------" '\n')
    f.write(f"Total Months: {len(months)}" '\n')
    f.write(f"Total: ${sum(profits)}" '\n')
    f.write(f"Average Change: ${averagechange:.2f}" '\n')
    f.write(f"Greatest Increase in Profits: {maxmonth} (${maxchange})" '\n')
    f.write(f"Greatest Decrease in Profits: {minmonth} (${minchange})" '\n')

    



    


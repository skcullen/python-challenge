# import needed modules
import os
import csv

#create empty lists to store the data
voters = []
candidatevote = []
canonevote = []
cantwovote = []
canthreevote = []
canfourvote = []
candidates = []
percentlist = []
countlist = []

#create path to needed data file
csvpath = os.path.join('Resources','election_data.csv')

#set up to read csv file, skipping the header
with open(csvpath, 'r') as electiondata:
    csvreader = csv.reader(electiondata, delimiter=',')
    csv_header = next(csvreader)

    #set up code to loop through rows
    for column in csvreader:

        #fill in lists with column data, will ultimately use this to calclate sum of voters
        voters.append(column[0])
        candidatevote.append(column[2])

    #create a list of candidates
    candidatelistset = set(candidatevote)
    #if running this code on new data, one must check how many candidates there are using the next line
    #the data this was run on has 4 candidates, but you will need to make changes if that is different
    #print(len(candidatelistset))

    #covert set into list so that it can be indexed in next step
    candidatelist = list(candidatelistset)

    #put each candidate from candidate list into a loop which sorts them out intotheir own individual list by candidate
    #if you have more or less candidates, you will have to edit the number of elifs, but the pattern is easily repeatable
    #you will have to change the number in all sequencial calculations
    #if changing number of candidates, remember to add/drop new empty lists at top
    for x in range(len(candidatevote)):
        if candidatevote[x-1] == candidatelist[0]:
            canonevote.append(candidatevote[x-1])
        elif candidatevote[x-1] == candidatelist[1]:
            cantwovote.append(candidatevote[x-1])
        elif candidatevote[x-1] == candidatelist[2]:
            canthreevote.append(candidatevote[x-1])
        elif candidatevote[x-1] == candidatelist[3]:
            canfourvote.append(candidatevote[x-1])

    #find percent of vote for each candidate (the percent sign will be added later)
    canonepercent = (len(canonevote)/len(voters))*100
    cantwopercent = (len(cantwovote)/len(voters))*100
    canthreepercent = (len(canthreevote)/len(voters))*100
    canfourpercent = (len(canfourvote)/len(voters))*100

    #find vote count for each candidate
    canonecount = (len(canonevote))
    cantwocount = (len(cantwovote))
    canthreecount = (len(canthreevote))
    canfourcount = (len(canfourvote))
    
    #put percentages into list
    percentlist.append(canonepercent)
    percentlist.append(cantwopercent)
    percentlist.append(canthreepercent)
    percentlist.append(canfourpercent)

    #put vote count into list
    countlist.append(canonecount)
    countlist.append(cantwocount)
    countlist.append(canthreecount)
    countlist.append(canfourcount)

    #use max of countlist or percentlist to find the winner
    if max(countlist) == canonecount:
        winner = candidatelist[0]
    elif max(countlist) == cantwocount:
        winner = candidatelist[1]
    elif max(countlist) == canthreecount:
        winner = candidatelist[2]
    elif max(countlist) == canfourcount:
        winner = candidatelist[3]

#create output data
print(f"Election Results")
print("-----------------------------")

#find sum of voters and print
print(f"Total Votes: {len(voters)}")
print("-----------------------------")

#candidate, percentage and vote count
print(f"{candidatelist[0]}: {canonepercent:.3f}% ({canonecount})") 
print(f"{candidatelist[1]}: {cantwopercent:.3f}% ({cantwocount})")
print(f"{candidatelist[2]}: {canthreepercent:.3f}% ({canthreecount})")
print(f"{candidatelist[3]}: {canfourpercent:.3f}% ({canfourcount})")
print("-----------------------------")

#print the winner
print(f"Winner: {winner}")
print("-----------------------------")


#export the results into a txt file
#write the path for where we want the results
output = os.path.join("analysis", "election_summary.txt")

#open file in write mode and fill in the output data
with open(output, 'w') as f:
    f.write("Election Results" '\n')
    f.write("-----------------------------" '\n')
    f.write(f"Total Votes: {len(voters)}" '\n')
    f.write("-----------------------------" '\n')
    f.write(f"{candidatelist[0]}: {canonepercent:.3f}% ({canonecount})"'\n')
    f.write(f"{candidatelist[1]}: {cantwopercent:.3f}% ({cantwocount})" '\n')
    f.write(f"{candidatelist[2]}: {canthreepercent:.3f}% ({canthreecount})" '\n')
    f.write(f"{candidatelist[3]}: {canfourpercent:.3f}% ({canfourcount})" '\n')
    f.write("-----------------------------" '\n')
    f.write(f"Winner: {winner}" '\n')
    f.write("-----------------------------" '\n')
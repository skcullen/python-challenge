# python-challenge

Unit 3: Python HOMEWORK 

Included in this repository is my solution for the Unit 3: Python Homework for the Georgia Tech Analytics Bootcamp.

We were ask to write Python scripts for two different sets of data: PyBank and PyPoll. Each data set has its own folder in the repository, which includes the main script, the csv file that the original data came in, and the txt file which logged the output of the script.

The first of the two data sets I will go over is the PyBank. This exercise is looking at simple bank records in order to draw some desirable conclusions and summerizations. The original data was contained in a csv file called budget_data.csv. We were tasked to take that data and calculate the following: total number of months, net total of profits/losses, the changes of profits/losses for each month, the average change of profits/losses overall, as well the greastest increase and decrease in profits/losses in the time period (including month and amount). 

The code I  used in order to gather all of these values was pretty straight forward. I made sure to be careful that lists start at 0 instead of one so that the computar was grabbing the correct data to calculate the sought after results. The code could have been shortened for some values like the average change (average change in Profits/Losses), but I decided to assign a variable to it and make it very clear what was being calculated rather than the shorter version of plugging the calculation into the print statement at the end. The  code can be used on any data in the same format. 

For the PyPoll exercise, we were given the original data in the form of th file election_data.csv. This dataset is the poll data from a small town, and we have been asked to it and come out with a summary of election results. We are looking for some basic values that everyone looks for when perusing election results: total number of votes, a list of candidates to receive votes, percentage of vots for each candidate, total number of votes for each candidate, and print the winner of the election.

THe only real stumbling block in this code happens when you are asked to get the list of candidates. For this particular data set there were 4 candidates, and the rest of the code is written to relect that fact. If one were to have a dataset that had more or less candidates, then they would have to go through the rest of the steps after the initial listing of the candidates in order to make sure that the rest of the calculations are run correctly for every candidate. This is clearly labelled in the code itself and expanding or reducing the number of candidates would be very straight forward, but it does take extra time. In order to ensure that the code runs correctly of a different set of data than election_data.csv, then one must run the commented out print statement in line 35 to check number of candidates, and adjust numbers of sequencial calculations to reflect the number of candidates.


Includes:
1. PyBank Folder
    a. the script named main.py
    b. Resources folder which holds the original file: budget_data.csv
    c. analysis folder which hold the output text file with the results: budget_summary.txt
2. Pypoll Folder
    a. the script named main.py
    b. Resources folder which holds the original file: election_data.csv
    c. analysis folder which hold the output text file with the results: election_summary.txt
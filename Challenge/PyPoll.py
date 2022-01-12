# The data we need to retreive.
import csv
import os

# Connect to the CSV using variable
file_to_load = os.path.join("election_results.csv")

#create a file to save to and open and write to it
file_to_save = os.path.join("analysis","election_analysis.txt")

#open the csv file
with open(file_to_load) as election_data:

#To Do: read and analyze the data here
#read the file object with the reader function
    file_reader = csv.reader(election_data)

#print each row in the CSV file
    for roe in next(file_reader):
        print(row)









#1. Total number of votes cast
#2. List of candidates
#3. % votes for each candidate
#4. total votes for each candidate
#5. winner



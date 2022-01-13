# The data we need to retreive.
import csv
import os

# Connect to the CSV using variable
file_to_load = os.path.join("election_results.csv")

#create a file to save to and open and write to it
file_to_save = os.path.join("analysis","election_analysis.txt")

#total votes variable
total_votes = 0

#create candidate list
candidate_options = []

#create vote count dictionary
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage= 0 

#open the csv file
with open(file_to_load) as election_data:

#To Do: read and analyze the data here
#read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

#print each row in the CSV file
    for row in file_reader:
        #2. add to the total vote count
        total_votes += 1
        
        candidate_name = row[2]
    
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    #save final vote count to text file
    txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    
    
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
       
         #print candidate summary
        print(candidate_results)
    
    #save to text file
        txt_file.write(candidate_results)


        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count= votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
        # 4. Print the candidate name and percentage of votes.
        
    #create and print winner summary 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    








    #3. % votes for each candidate
    #5. winner



# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   # Print each row in the CSV file.
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) /float(total_votes) * 100
            winning_candidate = ""
            winning_count = 0
            winning_percentage = 0
if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
         
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


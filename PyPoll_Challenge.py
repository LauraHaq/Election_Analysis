# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
from sys import int_info

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Initialize a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Initialize an empty string for the largest county turnout and variable for county voter turnout.
largest_county = ""
largest_countyvote = 0
largest_countypercentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load,'r') as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Use logical operator in decision statement to check if county name aquired is in the couty list created
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count while looping through rows.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as election_results_txt:
    
    # Print the final vote count (to terminal)       
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    election_results_txt.write(election_results)
    
    # 6a: Write a repetition statement with for loop to get the county from the county dictionary.
    for county_name in county_votes:
        
        # 6b: Create a variabe to retrieve the county vote count.
        votesbycounty =  county_votes[county_name]
        
        # 6c: Calculate the percentage of votes for the county.
        countypercentages= float(votesbycounty/ float(total_votes)) *100

        # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {countypercentages:.1f}% ({votesbycounty:,}) \n")
        print(county_results)

        # 6e: Save the county votes to a text file.
        election_results_txt.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votesbycounty > largest_countypercentage):
            largest_countypercentage = votesbycounty
            winning_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f'\n'
        f'-------------------------\n'
        f'Largest County Turnout = {winning_county}\n'
        f'-------------------------\n')
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    election_results_txt.write(winning_county_summary)

 # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        
        # Calculate the percentage of votes.
        vote_percentage= float(votes) / float(total_votes) * 100

        # Write the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        election_results_txt.write(candidate_results)

        # Determine winning candidate
        # Determine if votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Write winning candidate 
    winning_candidate_summary = ( 
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    election_results_txt.write(winning_candidate_summary)
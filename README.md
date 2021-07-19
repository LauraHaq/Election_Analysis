# Election Analysis

## Initial Project Overview

The Colorado Board of Elections requested an audit to be performed on election results of a particular race. I was instructed to use command lines in a python interpreter to produce a text file of the following: 
1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code, 1.58.2

## Summary 
The initial analysis of the election shows:
- There were 369,711 total votes casted in election.
- The Candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The Candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette, who received 23.0% of the vote and 85,213 number of votes.
 As shown snapshot of following image of my Visual Studio Code terminal of script.

![Screenshot 2021-07-16 115905](https://user-images.githubusercontent.com/86267773/125996215-e7110307-d139-456d-8205-daeb5797d55a.png)

## Overview of Election Audit
The election commission requested new information to be added to the project using the same data file. The previous script that was created to pull data about candidates was used again to pull data about each county with new variables using same code patterns. The following was the additional information needed:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Audit Election Results
The Python script using Visual Studio Code was successful in reading the same elections results to add additional findings to the initial analysis above:
- Vote turnout
    - Jefferson had 10.5% of the total vote turnout with 38,855 votes.
    - Denver had 82.8% of the total vote turnout with 306,055 votes.
    - Arapahoe had 6.7% of the total vote turnout with 24,801 votes. 
- The county with largest turnout:
    - Denver.
    
Updated terminal printed with adapted script:

![printed_terminal_electionresults](https://user-images.githubusercontent.com/86267773/126052354-846273e7-5709-4fd4-9469-76ec95175c1b.png)

Same results can also be found in shareable file using adapted script:
![election_results.txt](https://github.com/LauraHaq/Election_Analysis/files/6835487/election_results.txt)

## Election Audit Summary
In addition to finding the requested information for the audit, the overall analysis provides a tool that can be used in future election results. Firstly, it provides a working script that is usable on any completed election with any list of candidates and counties in a readable file with no modifications needed. Also, with some modification of variables the script can work with other demographic information to analyze vote turnout as well. Also modification of what would be printed in the results file would be needed to accurately reflect what is begin asked. This repetitive nature is first seen in the variables to create lists and dictionaries:
#### Initial analysis:
    - candidate_options = []
    - candidate_votes = {}
#### Audit challenge:
    - county_options = []
    - county_votes = {}
Also in how to begin tracking results:
#### Initial analysis:
    - winning_candidate = ""
    - winning_count = 0
    - winning_percentage = 0
#### Audit challenge:
    - largest_county = ""
    - largest_countyvote = 0
    - largest_countypercentage = 0

The additional information needed was found by adding the new variables into the initial for loops and can be used for any data requested as long as it is in a readable file that is in csv or column and row format.

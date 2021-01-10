# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

#file_path = "C:\\Users\\Patrice\\Python_Homework\\PyPoll\\Resources\\election_data.csv"
## To add new work and update our github repo:
## git init
## git add .
## git commit -m "message about changes"
## git push

total_votes=[]
candidates_list=[]
can_votes =[]

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")
    data_header = next(election_data)


    for row in reader:
        total_votes.append(row[0])

        candidate = row[2]
        if candidate in candidates_list:


    print(f"Total Votes: {len(total_votes)}")

#list of candidates 


# calculate percentage of votes 

#

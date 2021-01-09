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

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

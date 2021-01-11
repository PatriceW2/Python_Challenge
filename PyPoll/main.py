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

number_of_votes=[]
candidates_list=[]
can_votes =[]
percentages = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")
    data_header = next(election_data)


    for row in reader:
        number_of_votes.append(row[0])

        

        candidate = row[2]
        if candidate in candidates_list:
            candidate_index = candidates_list.index (candidate)
            can_votes[candidate_index] = can_votes[candidate_index] + 1
        else:
            candidates_list.append(candidate)   
            can_votes.append(1)
    
    khan_index = can_votes[0]
    correy_index = can_votes[1]
    li_index = can_votes[2]
    tooley_index = can_votes[3]

    

    khan_perc = khan_index/len(number_of_votes)*100
    
 



print(f"Total Votes: {len(number_of_votes)}")

print(f"{khan_perc}")






#list of candidates 


# calculate percentage of votes 

#

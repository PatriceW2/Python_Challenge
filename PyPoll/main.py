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
    
    for i in range(1, len(can_votes)):
        max_votes = max(can_votes)

        max_votes_index = can_votes.index(max_votes)
    

    khan_perc = can_votes[0]/len(number_of_votes)*100
    correy_perc = can_votes[1]/len(number_of_votes)*100
    li_perc = can_votes[2]/len(number_of_votes)*100
    tooley_perc = can_votes[3]/len(number_of_votes)*100



print("Election Results") 

print("---------------------")

print(f"Total Votes: {len(number_of_votes)}")

print("----------------------")

print(f"{candidates_list[0]}: {round(khan_perc, 4)}% {can_votes[0]}")

print(f"{candidates_list[1]}: {round(correy_perc, 4)}% {can_votes[1]}")

print(f"{candidates_list[2]}: {round(li_perc, 4)}% {can_votes[2]}")

print(f"{candidates_list[3]}: {round(tooley_perc, 4)}% {can_votes[3]}")

print("----------------------")

print(f"Winner: {candidates_list[max_votes_index]}")


#list of candidates 


# calculate percentage of votes 

#

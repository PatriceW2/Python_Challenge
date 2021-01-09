## To add new work and update our github repo:
## git init
## git add .
## git commit -m "message about changes"
## git push

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "financial_analysis.txt")


# Analyze the records to calculate the following
# Total number of months included in the data set
# net total amount of "profit/losses" over the entire period
# calculate changes in "profit/losses" over period,  then find averge of those changes
# greated increase in profits (date and amount)  over time
# greatest decrest in losses over time 

#assign empty lists (to be used later)

month_total = []
net_total = []
changes = []



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")
    data_header = next(election_data)



    for row in reader:
        month_total.append(row[0])

        net_total.append(int(row[1]))

month_total = len(month_total)

print(f"Total Months: {month_total}")

net_total = net_total + int(row[1])

print(f"Total: {net_total}")

























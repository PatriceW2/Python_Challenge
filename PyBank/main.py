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

#received help from tudor for the i loop and subsequent code

    for i in range(1, len(net_total)):
        changes.append(net_total[i] - net_total[i-1])

        ave_change = sum(changes)/len(changes)

        max_value = max(changes)

        max_value_index = changes.index(max_value) + 1

        min_value = min(changes)

        min_value_index = changes.index(min_value) + 1

#tudor helped point out that functions can be preformed in f print statments 

print("Finacial Analysis")

print("-----------------------")

print(f"Total Months: {len(month_total)}")


print(f"Total: ${sum(net_total)}")

print(f"Average Change: $ {round(ave_change, 2)}")

print(f"Greatest Increase in Profits: {month_total[max_value_index]} ${max_value}")

print(f"Greatest Decrease in Profits: {month_total[min_value_index]} ${min_value}")

file_to_output = os.path.join("PyBank", "Resources", "analysis", "financial_analysis.txt")



# define variable for average change

# find greatest month over month increase in profits 























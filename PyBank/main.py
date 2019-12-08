import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
bank_csv = os.path.join('budget_data.csv')


#variables

#total cols in first row. this will be used to average out
total_dates = 0

#total dollar mounts
total_dollars = 0

#list to append dollar values to 
total_volume_set = []

#empty list to use to call information from csv
dates =[]


#function that we will use to store budget info via lists
#we will store this via list in order to calculate the overall change data requested

def pybank(budget_data):
    date = budget_data[0]
    dates.append(date)
    change = int(budget_data[1])
    total_volume_set.append(change)


change_set = []
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_dates = total_dates + 1
        total_dollars += int(row[1])
        pybank(row)
    
    #this is a list to step through the total_volume_set list, subtracting the value in the previous value
    #this will give us a list of monthly changes that we can use to calculate average change

    change_set = [y-x for x, y in zip(total_volume_set, total_volume_set[1:])]

    #defining our variables
    avg = sum(change_set) / len(change_set)
    avg2 = round(avg,2)
    max_inc = max(change_set)
    max_dec = min(change_set)

    #since python lists start at 0, we add 1 to sync up the index values correctly
    #if you don't do this, the date that you call that corresponds to the max inc/dec will be off by 1

    max_inc_index = change_set.index(max_inc) + 1
    max_dec_index = change_set.index(max_dec) + 1

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_dates}")
    print(f"Total: ${total_dollars}")
    print(f"Average Change: ${avg2}")
    print(f"Greatest Increase in Profits:{dates[max_inc_index]} (${max_inc})")
    print(f"Greatest Decrease in Profits:{dates[max_dec_index]} (${max_dec})")
    
    
    output_file = open("budget_result.txt","w")
    output_file.write("Financial Analysis \n")
    output_file.write("---------------------------- \n")
    output_file.write(f"Total Months: {total_dates}\n")
    output_file.write(f"Total: ${total_dollars}\n")
    output_file.write(f"Average Change: ${avg2}\n")
    output_file.write(f"Greatest Increase in Profits: {dates[max_inc_index]} (${max_inc})\n")
    output_file.write(f"Greatest Decrease in Profits: {dates[max_dec_index]} (${max_dec})\n")
    output_file.close


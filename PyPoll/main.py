import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
poll_csv = os.path.join('election_data.csv')

#defining some variables...votes will get me the total vote count
#the empty lists are to place the appropriate voting results. this will determine the overall counts and winner

votes = 0
khan_votes =[]
correy_votes = []
li_votes = []
otooley_votes = []


#function to append voting results to the correct list

def pypoll(election_data):
    if election_data[2] == "Khan":
        khan_votes.append(election_data[0])
    elif election_data[2] == "Correy":
        correy_votes.append(election_data[0])
    elif election_data[2] == "Li":
        li_votes.append(election_data[0])
    else:
        otooley_votes.append(election_data[0])
    

with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    csvwriter = csv.writer(csvfile, delimiter = ',', quotechar='"',quoting=csv.QUOTE_MINIMAL)

    # Loop through the data
    for row in csvreader:
        votes = votes + 1
        pypoll(row)
    
    #basic numeric variables. i made them as descriptive as possible

    khan_pct = float((len(khan_votes) / votes) * 100)
    correy_pct = float((len(correy_votes) / votes) * 100)
    li_pct = float((len(li_votes) / votes)*100)
    otooley_pct = float((len(otooley_votes) / votes)*100)

    khan_pct_rounded = round(khan_pct,3)
    correy_pct_rounded = round(correy_pct,3)
    li_pct_rounded = round(li_pct,3)
    otooley_pct_rounded = round(otooley_pct,3)

    #this is a list to determine the final winner, you will take the max of this list and compare it to the lists created in the
    #function to determine the victor

    final_count = [len(khan_votes),len(correy_votes),len(li_votes),len(otooley_votes)]

    #if statement to determine the winner

    if max(final_count) == len(khan_votes):
        winner = "Khan"
    elif max(final_count) == len(correy_votes):
        winner = "Correy"
    elif max(final_count) == len(li_votes):
        winner = "Li"
    else:
        winner = "O'Tooley"



    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votes}")
    print("-------------------------")
    print(f"Khan:{khan_pct_rounded} % ({len(khan_votes)})")
    print(f"Correy:{correy_pct_rounded} % ({len(correy_votes)})")
    print(f"Li:{li_pct_rounded} % ({len(li_votes)})")
    print(f"O'Tooley:{otooley_pct_rounded} % ({len(otooley_votes)})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    output_file = open("election_result.txt","w")
    output_file.write("Election Results \n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {votes}\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Khan: {khan_pct_rounded}% ({len(khan_votes)})\n")
    output_file.write(f"Correy: {correy_pct_rounded}% ({len(correy_votes)})\n")
    output_file.write(f"Li: {li_pct_rounded}% ({len(li_votes)})\n")
    output_file.write(f"O'Tooley: {otooley_pct_rounded}% ({len(otooley_votes)})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

    output_file.close
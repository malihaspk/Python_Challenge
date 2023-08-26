#%%

import os
import csv

# Set path for file
#csvpath = os.path.join(r'C:\Users\user\Desktop\Python_week3\Python_Challenge\PyPoll\Resources\election_data.csv', "election_data.csv")
csvpath = os.path.join("Resources\election_data.csv","election_data.csv")

#open thecsv file
with open("Resources\election_data.csv", encoding='UTF-8') as csvfile:
     csv_reader = csv.reader(csvfile, delimiter=",")
     #Skip the header row
     next(csv_reader) 
     total_votes = 0
     candidate_votes = {}
     vote_casted=0
     for row in csv_reader:
        candidate_name = row[2]
        ballot = int(row[0])  # Assuming votes are stored as integers
        vote_casted += 1
        # Update the candidate_votes dictionary
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name].append(ballot)
        else:
            candidate_votes[candidate_name] = [ballot]
       
        # Calculate and print the candidate information
print("Election Results")
print()
print("----------------------------------\n")
print(f"Total Votes: {vote_casted}")
print("----------------------------------\n")


high_vote = 0
winner = ""
#print (candidate_votes)
for candidate, votes in candidate_votes.items():
    vote_count = len(votes)
    percentage = (vote_count /vote_casted ) * 100
    candidates=(f"{candidate:}\t\t{percentage:.3f}%\t\t({vote_count})")
    print (candidates)
    
#figuring out the winner
    
    if vote_count > high_vote:
        high_vote = vote_count
        winner = candidate
    
print("----------------------------------\n")
print(f"Winner: {winner} ")


 # setting the path to write file   
output_path = os.path.join("Analysis","results.txt")



#  Open the output file
with open(output_path, "w",newline='') as file:
    writer=csv.writer(file)
        #writing the Election results and total votes in results.txt
    results=(f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {vote_casted}\n"
    f"----------------------------------\n")
        
    file.write(results)
        #for loop to display the candidates information in results.txt
    for candidate,votes in candidate_votes.items():
            vote_count = len(votes)
            percentage = (vote_count /vote_casted ) * 100
    
            candidates=(f"{candidate:}\t\t\t{percentage:.3f}%\t\t({vote_count})")
            writer.writerow([candidates])
         #printing line  
            file.write("----------------------------------\n")
        #printing empty row
            writer.writerow([])
        #writing the winner in results.txt
            file.write(f"Winner: {winner} ")
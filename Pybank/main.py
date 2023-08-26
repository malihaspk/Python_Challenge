#%%

import os
import csv

# Set path for file

csvpath = os.path.join(r"Resources\budget_data.csv","budget_data.csv")


with open(r"Resources\budget_data.csv", encoding='UTF-8') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row
    #csv_header=next(csvfile)
    total_months=0
    totalprofit_loss = 0 
    changes_profitloss =0
    changes_profitloss=[]
    previous_value=0
    greatest_increase=0
    greatest_decrease=0
    greatestincrease_date=''
    greatestdecrease_date=''
    

    for row in csvreader:
        # Assuming the month is in the first column of each row
        date= row[0]
        total_months += 1
        profit_loss = int(row[1])  # Convert the value to an integer
        totalprofit_loss += profit_loss
        
         #if previous_value is not equal to 0    
        if previous_value !=0 :  
              change= profit_loss- previous_value
              changes_profitloss.append(change)
              
              if change> greatest_increase:
                 greatest_increase=  change
                 greatestincrease_date=date
              
              if change<greatest_decrease:
                 greatest_decrease=  change
                 greatestdecrease_date=date  
        
           
        previous_value=profit_loss
           #calcutale the average change for profit/loss amount
          
    totalchanges= sum(changes_profitloss)
    count_changesprofitloss=len(changes_profitloss)
    average_changes = round(sum (changes_profitloss)/len(changes_profitloss),2)
           
print("Financial Analysis")
print("--------------------------------\n")
print("Total months:", total_months)
print(f'Total:(${totalprofit_loss})')
print(f'Average change:(${average_changes})')
print(f'Greatest Increase in Profits: {greatestincrease_date}  (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatestdecrease_date}  (${greatest_decrease}) ')

output_path = os.path.join("Analysis","output.txt")
#Open the output file
with open(output_path, "w",newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        #writing the Financial Analysis in output.txt
        analysis=(f"Financial Analysis\n"
        f"----------------------------------\n"
        f"Total months: {total_months}\n"
        
        f"Total: {totalprofit_loss}\n"       
        f'Average change:(${average_changes})\n')
        file.write(analysis)
        file.write(f"Greatest Increase in Profits: {greatestincrease_date}  (${greatest_increase})\n")
        
        file.write(f"Greatest Decrease in Profits: {greatestdecrease_date} (${greatest_decrease})")
        
   
    
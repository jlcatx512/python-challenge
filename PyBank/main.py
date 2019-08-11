# Jadd Cheng August 10, 2019
# import dependencies
import os
import csv

# create csv_path
csv_path = os.path.join('Resources', 'budget_data.csv')
csv_path

with open (csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # skip header
    next(csv_reader) 
    
    csv_list = []
    for row in csv_reader:
        csv_list.append(row)

    change_count = 0
    change_sum = 0
    
    month_count = 0
    profit_loss_total = 0

    # New dict to keep track of changes. Use it to calculate greatest increase/decrease.
    change_dict = {}
    
    # Loop through each row to count entries, calculate total and average change.
    for i in range(len(csv_list)-1):
        month_count += 1
        current_row_amount = csv_list[i][1]
        next_row_amount = csv_list[i+1][1]
              
        change = int(next_row_amount) - int(current_row_amount)
    
    # Track running total of changes and count of entries.
        change_sum += int(change)
        change_count += 1
        
        monthyear = csv_list[i+1][0]
        if monthyear not in change_dict:
            change_dict[monthyear] = change
        
        profit_loss_total += int(current_row_amount)
        if i+1 == len(csv_list)-1:
            profit_loss_total += int(next_row_amount)
            month_count += 1
    
    # Calculate and format average change.
    average_change = change_sum/change_count
    if average_change >= 0:
        average_change = '${:.2f}'.format(average_change)
    else:
        average_change = '$-{:.2f}'.format(-average_change)

    # Calculate max and min increases. Convert dict into list.
    change_dict_keys = list(change_dict.keys())
    change_dict_values = list(change_dict.values())

    greatest_increase_date = change_dict_keys[change_dict_values.index(max(change_dict_values))]
    greatest_increase = change_dict[greatest_increase_date] # Relies on out of preceding line.

    greatest_decrease_date = change_dict_keys[change_dict_values.index(min(change_dict_values))]
    greatest_decrease = change_dict[greatest_decrease_date] # Relies on out of preceding line.

    # Print Financial Analysis.
    analysis = (
        f"""Financial Analysis\n"""
        f"""----------------------------\n"""
        f"""Total Months: {month_count}\n"""
        f"""Total: ${profit_loss_total}\n"""
        f"""Average  Change: {average_change}\n"""
        f"""Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"""
        f"""Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"""
        )
    print(analysis)

# print results to text file.
with open("pybank_financial_analysis_jadd_cheng.txt", "w") as text_file:
    print(analysis, file=text_file)
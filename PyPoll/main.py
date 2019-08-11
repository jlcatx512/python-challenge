# Jadd Cheng August 10, 2019

# Import dependencies
import os
import csv

# Create file path variable
csv_path = os.path.join('Resources', 'election_data.csv')
csv_path

with open (csv_path, newline='') as f: # f refers to the file
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader) # skip header row
    
    candidate_votes_dict = {} # key-value, candidates, votes
    candidate_percent_dict = {}
    total_votes = 0
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidate_votes_dict.keys():
            candidate_votes_dict[candidate] = 1
        else:
            candidate_votes_dict[candidate] += 1
            
    for candidate in candidate_votes_dict.keys():
        candidate_percent_dict[candidate] = '{:.3%}'.format(float(candidate_votes_dict[candidate]/total_votes))

# Determine winner.
v = list(candidate_votes_dict.values())
k = list(candidate_votes_dict.keys())

winner = k[v.index(max(v))]

# Print out Election Results to terminal.
print(f"""Election Results\n"""
      f"""-------------------------\n"""
    f"Total Votes: {total_votes}\n"
    f"""-------------------------""")
for candidate in candidate_votes_dict:
    print(f"{candidate}: {candidate_percent_dict[candidate]} ({candidate_votes_dict[candidate]})")
print(f"""-------------------------\n"""
      f"""Winner: {winner}\n"""
      f"""-------------------------""")

# Print Election Results to text file.
with open("pypoll_election_results_jadd_cheng.txt", "w") as text_file:
    print(f"""Election Results\n"""
          f"""-------------------------\n"""
        f"Total Votes: {total_votes}\n"
        f"""-------------------------""", file=text_file)
    for candidate in candidate_votes_dict:
        print(f"{candidate}: {candidate_percent_dict[candidate]} ({candidate_votes_dict[candidate]})", file=text_file)
    print(f"""-------------------------\n"""
          f"""Winner: {winner}\n"""
          f"""-------------------------""",  file=text_file)
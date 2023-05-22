import csv

poll_csv = r"C:\Users\Mason\python-challenge\PyPoll\Resources\election_data.csv"
text = r"C:\Users\Mason\python-challenge\PyPoll\analysis\analysis.txt"

total = 0
votes = {}
candidates = []

with open(poll_csv, 'r') as file:
    poll = csv.reader(file, delimiter=',')
    next(poll) 
    
    for row in poll:
        total += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

percentages = {}
for candidate in candidates:
    percentage = (votes[candidate] / total) * 100
    percentages[candidate] = percentage

winner = max(votes, key=votes.get)

output = "Election Results\n"
output += "-------------------------\n"
output += f"Total Votes: {total}\n"
output += "-------------------------\n"
for candidate in candidates:
    output += f"{candidate}: {percentages[candidate]:.3f}% ({votes[candidate]})\n"
output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += "-------------------------\n"

with open(text, "w") as Analysis:
    Analysis.write(output)
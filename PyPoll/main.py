import pandas as pd
from pathlib import Path

file_path = Path("Resources/election_data.csv")
election_df = pd.read_csv(file_path)

#total votes
total_votes = election_df.shape[0]

#candidates and votes
candidate_votes = election_df['Candidate'].value_counts()

#percentage of votes
percentage_votes = (candidate_votes / total_votes) * 100

#winner index max
winner = candidate_votes.idxmax()

#print
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_path = Path('analysis')/"election_results.txt"
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
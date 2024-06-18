import pandas as pd
from pathlib import Path

file = Path("Resources/budget_data.csv")
budget_df = pd.read_csv(file)
budget_df.head()

total_months = budget_df['Date'].count()

#total of p/l
total_pl = budget_df['Profit/Losses'].sum()

budget_df.loc[:, 'Profit/Losses'] = budget_df['Profit/Losses'].diff()

#mean of p/l change
mean_change = budget_df['Profit/Losses'].mean()

#biggest increase
highest_increase = budget_df.loc[budget_df['Profit/Losses'].idxmax()]

#biggest decrease
greatest_decrease = budget_df.loc[budget_df['Profit/Losses'].idxmin()]


#print 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average Change: ${mean_change:.2f}")
print(f"Greatest Increase in Profits: {highest_increase['Date']} (${int(highest_increase['Profit/Losses'])})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${int(greatest_decrease['Profit/Losses'])})")

output_path = Path('analysis') / 'financial_analysis.txt'

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_pl}\n")
    file.write(f"Average Change: ${mean_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {highest_increase['Date']} (${highest_increase['Profit/Losses']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit/Losses']})\n")

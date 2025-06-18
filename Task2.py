import pandas as pd
import matplotlib.pyplot as plt

data_file = pd.ExcelFile('dataset3.xlsx')
sheets_to_process = ['A', 'C', 'D', 'W']

bug_counts = {}

for sheet in sheets_to_process:
    sheet_data = data_file.parse(sheet)
    bug_counts[sheet] = sheet_data[sheet_data['type'] == 'Bug'].shape[0]

sorted_bug_counts = dict(sorted(bug_counts.items(), key=lambda item: item[1], reverse=True))

cumulative_percentage = (pd.Series(sorted_bug_counts).cumsum() / sum(sorted_bug_counts.values())) * 100

fig, ax1 = plt.subplots()

ax1.bar(sorted_bug_counts.keys(), sorted_bug_counts.values(), color='g', alpha=0.7, label='Number of Bugs')
ax1.set_xlabel('Module')
ax1.set_ylabel('Number of Bugs', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(sorted_bug_counts.keys(), cumulative_percentage, color='r', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage', color='pink')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.title('Pareto Diagram - Number of Bugs per Module')
plt.show()

most_bugs_module = list(sorted_bug_counts.keys())[0]
print(f"The module '{most_bugs_module}' has the most bugs with {sorted_bug_counts[most_bugs_module]} bugs reported.")

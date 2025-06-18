import pandas as pd
import matplotlib.pyplot as plt

# Load dataset 3
df3 = pd.read_excel("dataset3.xlsx")

# Group by 'assignee' and count the number of bugs for each
assignee_bug_counts = df3['assignee'].value_counts()

# Calculate the cumulative percentage
C_per = assignee_bug_counts.cumsum() / assignee_bug_counts.sum() * 100

top_assignee = assignee_bug_counts.idxmax()
top_assignee_count = assignee_bug_counts.max()

print(f"The assignee with the most bugs to resolve is {top_assignee} with {top_assignee_count} bugs.")

fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.bar(assignee_bug_counts.index, assignee_bug_counts, color='b', alpha=0.6, label='No. of Bugs')
ax1.set_xlabel('Assignee')
ax1.set_ylabel('No. of Bugs', color='b')
ax1.tick_params('y', colors='b')
ax1.set_title('Pareto Diagram for Number of Bugs per Assignee')
plt.xticks(rotation=90)

ax2 = ax1.twinx()
ax2.plot(C_per.index, C_per, color='r', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative (%)age', color='g')
ax2.tick_params('y', colors='r')
ax2.grid(None)

plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df_dataset3 = pd.read_excel('dataset3.xlsx')

bugs = df_dataset3[df_dataset3['status'].str.strip() != 'Closed']

count = bugs['assignee'].value_counts()

c_per = (count / count.sum()).cumsum()

# Plot the Pareto diagram
fig, ax1 = plt.subplots()

ax1.bar(count.index, count, color='b', alpha=0.7, label='Bugs(Open) Assigned')
ax1.set_xlabel('Assignee')
ax1.set_ylabel('No. of Open Bugs Assigned', color='b')
ax1.tick_params('y', colors='b')
plt.xticks(rotation=90)

ax2 = ax1.twinx()
ax2.plot(count.index, c_per, color='r', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.title('Pareto Chart - Open Bugs Assigned')
plt.show()

top_assignee = count.idxmax()
print(f"The assignee given the most bugs to resolve and they are still not closed is: {top_assignee}")



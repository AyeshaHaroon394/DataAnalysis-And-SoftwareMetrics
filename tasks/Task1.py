import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_excel("dataset3.xlsx")

df1['component'] = df1['component'].str.strip()
df1['priority'] = df1['priority'].str.strip()

expanded_components = df1['component'].str.split(';', expand=True).stack().str.strip().reset_index(level=1, drop=True)
expanded_df = df1.drop('component', axis=1).join(expanded_components.rename('component'))

top_components = expanded_df['component'].value_counts().head(10).index.tolist()

filtered_df = expanded_df[expanded_df['component'].isin(top_components)]

plt.figure(figsize=(20, 15))
sns.countplot(data=filtered_df, y='component', hue='priority', order=top_components)
plt.title('Distribution of Issues by Priority for Top Components')
plt.xlabel('Number of Issues')
plt.ylabel('Top Components')
plt.legend(title='Issue Priority')
plt.show()

data1 = pd.read_excel("dataset1.xlsx")
data2 = pd.read_excel("dataset2.xlsx")

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 12))

sns.countplot(data=data2, x='Priority', order=data2['Priority'].value_counts().index, ax=axes[1])
axes[1].set_title('Distribution of Issues by Priority for Dataset 2')
axes[1].set_ylabel('Number of Issues')
axes[1].set_xlabel('Issue Priority')

plt.tight_layout()
plt.show()

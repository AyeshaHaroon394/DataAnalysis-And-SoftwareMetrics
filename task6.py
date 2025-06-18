import pandas as pd

# Load dataset 2
data_df2 = pd.read_excel("dataset2.xlsx")
print(data_df2.head())

# Create a filtered DataFrame, removing rows with missing values in 'Estimated time' and 'Spent time (hrs)'
filtered_data_df2 = data_df2.dropna(subset=['Estimated time', 'Spent time (hrs)']).copy()

# Calculate the Schedule Estimation Accuracy
filtered_data_df2['Schedule Estimation Accuracy'] = ((filtered_data_df2['Spent time (hrs)'] - filtered_data_df2['Estimated time']) / filtered_data_df2['Estimated time']) * 100

# Display relevant columns in the filtered DataFrame
relevant_columns = ['ID', 'Estimated time', 'Spent time (hrs)', 'Schedule Estimation Accuracy']
print(filtered_data_df2[relevant_columns])

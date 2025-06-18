import pandas as pd

#dataset 2
data_df2 = pd.read_excel("dataset2.xlsx")
data_df2['Start date'] = pd.to_datetime(data_df2['Start date'], errors='coerce')
data_df2['Finish date'] = pd.to_datetime(data_df2['Finish date'], errors='coerce')
data_df2['Fix Response Time (Days)'] = (data_df2['Finish date'] - data_df2['Start date']).dt.days
mean_fix_time_df2 = data_df2['Fix Response Time (Days)'].mean()
print(f"Mean Fix Response Time for Dataset 2: {mean_fix_time_df2} days")
#dataset 3
data_df3 = pd.read_excel("dataset3.xlsx")
data_df3['created'] = pd.to_datetime(data_df3['created'], errors='coerce')
data_df3['resolved'] = pd.to_datetime(data_df3['resolved'], errors='coerce')
data_df3['Fix Response Time (Days)'] = (data_df3['resolved'] - data_df3['created']).dt.days
mean_fix_time_df3 = data_df3['Fix Response Time (Days)'].mean()
print(f"Mean Fix Response Time for Dataset 3: {mean_fix_time_df3} days")

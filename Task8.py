import pandas as pd
import matplotlib.pyplot as plt

#dataset 2
data_df2 = pd.read_excel("dataset2.xlsx")
data_df2['Start date'] = pd.to_datetime(data_df2['Start date'], errors='coerce')
data_df2['Finish date'] = pd.to_datetime(data_df2['Finish date'], errors='coerce')
data_df2['Discovery Month'] = data_df2['Start date'].dt.to_period('M')
data_df2['Closure Month'] = data_df2['Finish date'].dt.to_period('M')

#grouping
discovered_df2 = data_df2.groupby('Discovery Month').size()
closed_df2 = data_df2.groupby('Closure Month').size()
bmi_df2 = (closed_df2 / discovered_df2 * 100).dropna()

#plotting
bmi_df2.plot(title="Business Monthly Index (BMI) for Dataset 2", ylabel="BMI (%)", xlabel="Month", grid=True)
plt.tight_layout()
plt.show()

#dataset 3
data_df3 = pd.read_excel("dataset3.xlsx")
data_df3['created'] = pd.to_datetime(data_df3['created'], errors='coerce')
data_df3['resolved'] = pd.to_datetime(data_df3['resolved'], errors='coerce')
data_df3['Discovery Month'] = data_df3['created'].dt.to_period('M')
data_df3['Closure Month'] = data_df3['resolved'].dt.to_period('M')
#Grouping
discovered_df3 = data_df3.groupby('Discovery Month').size()
closed_df3 = data_df3.groupby('Closure Month').size()
bmi_df3 = (closed_df3 / discovered_df3 * 100).dropna()
#Plotting
bmi_df3.plot(title="Business Monthly Index (BMI) for Dataset 3", ylabel="BMI (%)", xlabel="Month", grid=True)
plt.tight_layout()
plt.show()

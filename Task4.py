import pandas as pd
import matplotlib.pyplot as plt

def calculate_percent_delinquent_fixes_monthwise(dataframe, created_column, resolved_column):

    dataframe[created_column] = pd.to_datetime(dataframe[created_column], errors='coerce')
    dataframe[resolved_column] = pd.to_datetime(dataframe[resolved_column], errors='coerce')

    dataframe['Fix Response Time (Hours)'] = (dataframe[resolved_column] - dataframe[created_column]).dt.total_seconds() / 3600

    delinquent_fixes = dataframe[dataframe['Fix Response Time (Hours)'] > 4]

    monthly_delinquent_fixes = delinquent_fixes.groupby(delinquent_fixes[created_column].dt.to_period("M")).size()

    monthly_total_fixes = dataframe.groupby(dataframe[created_column].dt.to_period("M")).size()

    monthly_delinquent_fixes = monthly_delinquent_fixes.reindex(monthly_total_fixes.index, fill_value=0)

    pdf = (monthly_delinquent_fixes / monthly_total_fixes) * 100

    return pdf

data_df2 = pd.read_excel('dataset2.xlsx', parse_dates=['Start date', 'Finish date'])
data_df3_all_modules = pd.read_excel('dataset3.xlsx', sheet_name='All Modules')

#pdf for dataset 2
pdf_data_df2 = calculate_percent_delinquent_fixes_monthwise(data_df2, 'Start date', 'Finish date')

# PDF for dataset 3 all modules
pdf_data_df3_all_modules = calculate_percent_delinquent_fixes_monthwise(data_df3_all_modules, 'created', 'resolved')

# chart for dataset 2
plt.figure(figsize=(12, 6))
plt.plot(pdf_data_df2.index.strftime('%Y-%m'), pdf_data_df2.values, marker='o', linestyle='-')
plt.title('Time Run Chart for Percent Delinquent Fixes (PDF) - Dataset 2')
plt.xlabel('Month')
plt.ylabel('Percent Delinquent Fixes (%)')
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()

# display
plt.show()

# run chart for dataset 3
plt.figure(figsize=(12, 6))
plt.plot(pdf_data_df3_all_modules.index.strftime('%Y-%m'), pdf_data_df3_all_modules.values, marker='o', linestyle='-')
plt.title('Time Run Chart for Percent Delinquent Fixes (PDF) - Dataset 3 (All Modules)')
plt.xlabel('Month')
plt.ylabel('Percent Delinquent Fixes (%)')
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()

# display
plt.show()

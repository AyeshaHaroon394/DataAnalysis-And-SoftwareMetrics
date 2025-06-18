import pandas as pd

def calculate_fix_resolution_rate_monthwise(data, created_column, resolved_column):
    # Convert to datetime and calculate the fix resolution time in hours
    data[created_column] = pd.to_datetime(data[created_column], errors='coerce')
    data[resolved_column] = pd.to_datetime(data[resolved_column], errors='coerce')
    data['Fix Resolution Time (Hours)'] = (data[resolved_column] - data[created_column]).dt.total_seconds() / 3600
    delinquent_fixes = data[data['Fix Resolution Time (Hours)'] > 4]
    monthly_delinquent_fixes = delinquent_fixes.groupby(
        [delinquent_fixes[created_column].dt.year, delinquent_fixes[created_column].dt.month]).size()

    monthly_total_fixes = data.groupby([data[created_column].dt.year, data[created_column].dt.month]).size()

    full_date_range = pd.date_range(start=data[created_column].min(), end=data[created_column].max(), freq='M')
    full_index = [(date.year, date.month) for date in full_date_range]

    monthly_delinquent_fixes = monthly_delinquent_fixes.reindex(full_index, fill_value=0)
    monthly_total_fixes = monthly_total_fixes.reindex(full_index, fill_value=1)  # Use 1 to avoid division by zero

    pdf = (monthly_delinquent_fixes / monthly_total_fixes) * 100

    return pdf

pd.set_option('display.max_rows', None)
pd.options.display.float_format = '{:.2f}%'.format
data_df2 = pd.read_excel('dataset2.xlsx', parse_dates=['Start date', 'Finish date'])
data_df3_all_modules = pd.read_excel('dataset3.xlsx', sheet_name='All Modules')
pdf_data_df2 = calculate_fix_resolution_rate_monthwise(data_df2, 'Start date', 'Finish date')

pdf_data_df3_all_modules = calculate_fix_resolution_rate_monthwise(data_df3_all_modules, 'created', 'resolved')

# Print results
print("Fix Resolution Rate (PDF) for dataset 2:")
print(pdf_data_df2)
print("\nFix Resolution Rate (PDF) for dataset 3:")
print(pdf_data_df3_all_modules)

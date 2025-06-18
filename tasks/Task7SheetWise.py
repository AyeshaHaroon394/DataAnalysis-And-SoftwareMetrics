import pandas as pd
excel_file = pd.ExcelFile('dataset3.xlsx')

sheets = {
    'Sheet_A': excel_file.parse('A'),
    'Sheet_C': excel_file.parse('C'),
    'Sheet_D': excel_file.parse('D'),
    'Sheet_W': excel_file.parse('W'),
    'All Modules': excel_file.parse(0)
}

def calculate_mean_fix_response_time(dataframe):
    created_column = next((col for col in dataframe.columns if col.strip().lower() == 'created'), None)
    resolved_column = next((col for col in dataframe.columns if col.strip().lower() == 'resolved'), None)

    if not created_column or not resolved_column:
        return None

    dataframe[created_column] = pd.to_datetime(dataframe[created_column], errors='coerce')
    dataframe[resolved_column] = pd.to_datetime(dataframe[resolved_column], errors='coerce')

    valid_rows = dataframe.dropna(subset=[created_column, resolved_column]).index

    dataframe.loc[valid_rows, 'Fix Response Time (Days)'] = (
        dataframe.loc[valid_rows, resolved_column] - dataframe.loc[valid_rows, created_column]).dt.days

    return dataframe.loc[valid_rows, 'Fix Response Time (Days)'].mean()

for sheet_name, data in sheets.items():
    mean_fix_time = calculate_mean_fix_response_time(data)
    if mean_fix_time is not None:
        print(f"Module: {sheet_name}, Mean Fix Response Time: {mean_fix_time:.2f} days")
    else:
        print(f"Module: {sheet_name} does not have the required columns ('Created' and 'Resolved')")

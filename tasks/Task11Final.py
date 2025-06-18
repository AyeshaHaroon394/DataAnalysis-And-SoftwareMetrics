import pandas as pd

# Load the Excel file
xl = pd.ExcelFile('dataset3.xlsx')

# Extract sheets from the Excel file
sheet_A = xl.parse('A')
sheet_C = xl.parse('C')
sheet_D = xl.parse('D')
sheet_W = xl.parse('W')
first_sheet = xl.parse(0)  # Assuming the first sheet doesn't have a name provided

# Combine data from different sheets
combined_data = pd.concat([sheet_A, sheet_C, sheet_D, sheet_W, first_sheet])

def calculate_bug_ratio(dataframe):
    total_issues = dataframe['type'].count()
    num_bugs = dataframe[dataframe['type'] == 'Bug'].shape[0]
    proportion_bugs = num_bugs / total_issues
    percentage_bugs = proportion_bugs * 100
    return proportion_bugs, percentage_bugs

total_proportion, total_percentage = calculate_bug_ratio(combined_data)
print(f"Total Proportion of Bugs: {total_proportion}, Total Percentage of Bugs: {total_percentage}%")

sheets = {'Sheet A': sheet_A, 'Sheet C': sheet_C, 'Sheet D': sheet_D, 'Sheet W': sheet_W, 'First Sheet': first_sheet}
for sheet_name, data in sheets.items():
    prop, perc = calculate_bug_ratio(data)
    print(f"{sheet_name} - Bug Proportion: {prop}, Bug Percentage: {perc}%")

modules = combined_data['component'].unique()
for module in modules:
    prop, perc = calculate_bug_ratio(combined_data[combined_data['component'] == module])
    print(f"Module {module} - Bug Proportion: {prop}, Bug Percentage: {perc}%")

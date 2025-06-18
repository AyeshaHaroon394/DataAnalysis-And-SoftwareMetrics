import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate PDF
def calculate_percent_delinquent_fixes_monthwise(data, created_col, resolved_col):
    data[created_col] = pd.to_datetime(data[created_col], errors='coerce')
    data[resolved_col] = pd.to_datetime(data[resolved_col], errors='coerce')
    data['Fix Resolution Time (Hours)'] = (data[resolved_col] - data[created_col]).dt.total_seconds() / 3600

    delinquent_fixes = data[data['Fix Resolution Time (Hours)'] > 4]

    monthly_delinquent_fixes = delinquent_fixes.groupby(
        [delinquent_fixes[created_col].dt.year, delinquent_fixes[created_col].dt.month]).size()

    monthly_total_fixes = data.groupby([data[created_col].dt.year, data[created_col].dt.month]).size()

    full_date_range = pd.date_range(start=data[created_col].min(), end=data[created_col].max(), freq='M')
    full_index = [(date.year, date.month) for date in full_date_range]

    monthly_delinquent_fixes = monthly_delinquent_fixes.reindex(full_index, fill_value=0)
    monthly_total_fixes = monthly_total_fixes.reindex(full_index, fill_value=1)

    pdf = (monthly_delinquent_fixes / monthly_total_fixes) * 100

    return pdf

data_df2 = pd.read_excel('dataset2.xlsx', parse_dates=['Start date', 'Finish date'])
data_df3_all_modules = pd.read_excel('dataset3.xlsx', sheet_name='All Modules')
pdf_data_df2 = calculate_percent_delinquent_fixes_monthwise(data_df2, 'Start date', 'Finish date')
pdf_data_df3_all_modules = calculate_percent_delinquent_fixes_monthwise(data_df3_all_modules, 'created', 'resolved')


# Control Chart
def plot_control_chart(pdf_data, std_deviation, upper_limit, lower_limit, highlight_color):
    plt.figure(figsize=(12, 6))

    x = np.arange(len(pdf_data))

    plt.plot(x, pdf_data, marker='o', linestyle='-', color='blue', label='PDF')

    plt.xticks(x, pdf_data.index, rotation=90)

    plt.axhline(y=upper_limit, color='red', linestyle='--', label='Upper Control Limit', linewidth=2)
    plt.axhline(y=lower_limit, color='green', linestyle='--', label='Lower Control Limit', linewidth=2)

    out_of_control = (pdf_data > upper_limit) | (pdf_data < lower_limit)
    plt.scatter(x[out_of_control], pdf_data[out_of_control], color=highlight_color, label='Out of Control', zorder=5)

    plt.title('Control Chart for PDF')
    plt.xlabel('Time (Year-Month)')
    plt.ylabel('PDF (%)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

pdf_std_deviation = pdf_data_df3_all_modules.std()

pdf_mean = pdf_data_df3_all_modules.mean()
upper_limit = pdf_mean + 2 * pdf_std_deviation
lower_limit = pdf_mean - 2 * pdf_std_deviation
plot_control_chart(pdf_data=pdf_data_df3_all_modules, std_deviation=pdf_std_deviation, upper_limit=upper_limit,
                   lower_limit=lower_limit, highlight_color='orange')

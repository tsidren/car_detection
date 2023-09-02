import pandas as pd

# Specify the file path of the CSV file
csv_file = '../data/vehicle_details.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

licence_plate_digits = 6

# Filter the DataFrame based on the condition
filtered_df = df[(df.iloc[:, 1].str.len() >= licence_plate_digits) & (~df.iloc[:, 1].duplicated())]

# Save the filtered DataFrame to a new CSV file
output_file = '../data/filtered_file.csv'
filtered_df.to_csv(output_file, index=False)

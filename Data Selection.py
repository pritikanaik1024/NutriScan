import pandas as pd

# Load the CSV file with tab delimiter and low_memory=False
df = pd.read_csv('foodfacts.csv', delimiter='\t', on_bad_lines='skip', low_memory=False)

# Print initial columns
print("Initial columns:")
print(df.columns)

# List of columns to drop
columns_to_drop = [
    ['creator', 'url'],
]

# Drop columns if they exist in the DataFrame
for cols in columns_to_drop:
    cols_to_drop = [col for col in cols if col in df.columns]
    if cols_to_drop:
        df = df.drop(cols_to_drop, axis=1)

# Print columns after dropping
print("\nColumns after dropping:")
print(df.columns)

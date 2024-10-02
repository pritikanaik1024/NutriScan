import pandas as pd

# Load the dataset (adjust file path as necessary)
file_path = 'C:/Users/pritika naik/Downloads/en.openfoodfacts.org.products.tsv'
df = pd.read_csv(file_path, delimiter='\t', low_memory=False, on_bad_lines='skip')

# Keep only the 'code' column
df_code_only = df[['code']]

# Save the filtered DataFrame to a new CSV file
df_code_only.to_csv('Barcode_Dataset.csv', index=False)
print("Filtered dataset saved as 'Barcode_Dataset.csv'.")

import pandas as pd
from sklearn.preprocessing import StandardScaler
file_path = 'All_Diets.csv'
df = pd.read_csv(file_path)
# Now apply the string operation
df['Diet_type'] = df['Diet_type'].astype(str)
df['Diet_type'] = df['Diet_type'].str.lower()
df['Recipe_name'] = df['Diet_type'].astype(str)
df['Recipe_name'] = df['Diet_type'].str.lower()

print(df.head())
print(df.info())
print(df.describe())
print(df.head())
print(df.isnull().sum())
# Handle missing values
df = df.dropna()
# Remove duplicate rows
df = df.drop_duplicates()
# Verify no duplicates remain
print(df.duplicated().sum())
# Display the updated DataFrame information
print(df.info())

# Preprocess the dataset (example preprocessing, adjust as needed)
df = df.drop(columns=['Extraction_day', 'Extraction_time'])

from sklearn.preprocessing import StandardScaler
# Normalize numerical columns
scaler = StandardScaler()
df[['Protein(g)', 'Carbs(g)', 'Fat(g)']] = scaler.fit_transform(df[['Protein(g)', 'Carbs(g)', 'Fat(g)']])
# Save the preprocessed dataset
df.to_csv('Preprocessed_Diet_Dataset.csv', index=False)
print("Dataset has been preprocessed and saved as 'Preprocessed_Diet_Dataset.csv'")

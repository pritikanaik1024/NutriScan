# import pandas as pd
# import csv

# # File path to the dataset
# file_path = 'C:/Users/pritika naik/Downloads/en.openfoodfacts.org.products.tsv'
# chunksize = 10000  # Number of rows per chunk

# # Columns you want to keep
# columns_to_keep = [
#     "product_name", "generic_name", "quantity", "brands", "brands_tags", "categories", "categories_tags",
#     "categories_en", "labels", "labels_tags", "labels_en", "countries", "countries_tags", "countries_en",
#     "ingredients_text", "allergens", "allergens_en", "serving_size", "no_nutriments", "additives_n", "additives",
#     "additives_tags", "additives_en", "nutrition_grade_uk", "nutrition_grade_fr", "main_category", "main_category_en",
#     "image_url", "energy_100g", "fat_100g", "saturated_fat_100g", "monounsaturated_fat_100g",
#     "polyunsaturated_fat_100g", "trans_fat_100g", "cholesterol_100g", "carbohydrates_100g", "sugars_100g",
#     "lactose_100g", "starch_100g", "fiber_100g", "proteins_100g", "salt_100g", "sodium_100g", "alcohol_100g",
#     "fruits_vegetables_nuts_100g", "collagen_meat_protein_ratio_100g", "nutrition_score_fr_100g",
#     "nutrition_score_uk_100g"
# ]

# # Initialize list to store chunks
# df_list = []

# # Read the file in chunks and handle formatting issues
# try:
#     for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunksize, engine='c', 
#                              quoting=csv.QUOTE_NONE, quotechar='"', on_bad_lines='skip'):
#         # Ensure only the columns that exist in the chunk are selected
#         existing_columns = [col for col in columns_to_keep if col in chunk.columns]
#         if existing_columns:
#             # Filter and drop rows where 'product_name' is missing
#             df_filtered_chunk = chunk[existing_columns].dropna(subset=['product_name'])
#             df_list.append(df_filtered_chunk)

#     # Concatenate all chunks
#     if df_list:
#         df_filtered = pd.concat(df_list)

#         # Save the preprocessed data to CSV
#         df_filtered.to_csv('Preprocessed_Nutritional_Dataset.csv', index=False)

#         print("Preprocessing complete. Dataset saved as 'Preprocessed_Nutritional_Dataset.csv'.")
#     else:
#         print("No data was processed. Please check the dataset or column names.")

# except Exception as e:
#     print(f"An error occurred: {e}")



import pandas as pd

# Define file paths
barcode_dataset_path = r'C:\Users\pritika naik\Documents\GitHub\NutriScan\Barcode_Dataset.csv'
nutritional_dataset_path = r'C:\Users\pritika naik\Documents\GitHub\NutriScan\Preprocessed_Nutritional_Dataset.csv'

# Load the datasets
barcode_df = pd.read_csv(barcode_dataset_path)
nutritional_df = pd.read_csv(nutritional_dataset_path)

# Ensure the barcode column exists in the barcode dataset
if 'code' not in barcode_df.columns:
    raise ValueError("The barcode dataset must contain a 'code' column.")

# Create a new DataFrame to hold the joined data
joined_df = pd.concat([barcode_df, nutritional_df], axis=1)

# Save the joined DataFrame to a new CSV file
joined_df.to_csv('NutriScan_Dataset.csv', index=False)

print("Datasets have been joined and saved as 'NutriScan_Dataset.csv'.")

# 'C:/Users/pritika naik/Downloads/en.openfoodfacts.org.products.tsv'  
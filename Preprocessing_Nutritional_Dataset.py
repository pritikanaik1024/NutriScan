import pandas as pd
import csv
#
# # Define the columns to keep
# columns_to_keep = [
#     "code", "product_name", "generic_name", "quantity", "brands", "brands_tags", "categories", "categories_tags",
#     "categories_en", "labels", "labels_tags", "labels_en", "countries", "countries_tags", "countries_en",
#     "ingredients_text", "allergens", "allergens_en", "serving_size", "no_nutriments", "additives_n", "additives",
#     "additives_tags", "additives_en", "nutrition_grade_uk", "nutrition_grade_fr", "main_category", "main_category_en",
#     "image_url", "energy_100g", "fat_100g", "saturated_fat_100g", "monounsaturated_fat_100g",
#     "polyunsaturated_fat_100g", "trans_fat_100g", "cholesterol_100g", "carbohydrates_100g", "sugars_100g",
#     "lactose_100g", "starch_100g", "fiber_100g", "proteins_100g", "salt_100g", "sodium_100g", "alcohol_100g",
#     "fruits_vegetables_nuts_100g", "collagen_meat_protein_ratio_100g", "nutrition_score_fr_100g",
#     "nutrition_score_uk_100g"
# ]
#
# # Define a larger chunk size
# chunk_size = 500000  # Adjust based on your memory capacity
#
# # Process the file in chunks and save each chunk to a separate CSV
# for i, chunk in enumerate(
#         pd.read_csv('data.csv', delimiter='\t', low_memory=False, on_bad_lines='skip', chunksize=chunk_size)):
#
#     # Clean column names
#     chunk.columns = chunk.columns.str.strip().str.lower()
#
#     # Select only the columns we need (case-insensitive match)
#     available_columns = [col for col in columns_to_keep if col.lower() in chunk.columns]
#
#     # Filter the chunk to keep only the necessary columns
#     chunk = chunk[available_columns]
#
#     # Fill NaNs with empty strings only for object (string) columns
#     chunk = chunk.fillna('') if chunk.select_dtypes(include=[object]).shape[1] > 0 else chunk
#
#     # Ensure consistent formatting for string columns
#     chunk = chunk.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
#
#     # Keep 'code' as a string to avoid overflow issues
#     if 'code' in chunk.columns:
#         chunk['code'] = chunk['code'].astype(str)
#
#     # Save the processed chunk to a CSV file
#     chunk.to_csv(f'Preprocessed_Chunk_{i}.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
#
# print("Data preprocessing complete. Chunks saved as 'Preprocessed_Chunk_*.csv'.")
#

# Load the preprocessed data
df = pd.read_csv('Preprocessed_Nutritional_Dataset.csv', delimiter=',')

# Save the DataFrame to a new CSV file with proper quoting
df.to_csv('Formatted_Nutritional_Dataset.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

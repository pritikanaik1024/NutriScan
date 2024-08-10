import pandas as pd

# Read the first row to get column names
df_sample = pd.read_csv('food_details.tsv', delimiter='\t', nrows=1, on_bad_lines='skip')
actual_columns = [col.strip() for col in df_sample.columns.tolist()]
print("Actual Columns:", actual_columns)

# Adjusted list of columns to keep based on actual column names
columns_to_keep = [
    "code", "product_name", "generic_name", "quantity", "brands", "brands_tags", "categories", "categories_tags",
    "categories_en", "labels", "labels_tags", "labels_en", "countries", "countries_tags", "countries_en",
    "ingredients_text", "allergens", "allergens_en", "serving_size", "no_nutriments", "additives_n", "additives",
    "additives_tags", "additives_en", "nutrition_grade_uk", "nutrition_grade_fr", "main_category", "main_category_en",
    "image_url", "energy_100g", "fat_100g", "saturated_fat_100g", "monounsaturated_fat_100g",
    "polyunsaturated_fat_100g", "trans_fat_100g", "cholesterol_100g", "carbohydrates_100g", "sugars_100g",
    "lactose_100g", "starch_100g", "fiber_100g", "proteins_100g", "salt_100g", "sodium_100g", "alcohol_100g",
    "fruits_vegetables_nuts_100g", "collagen_meat_protein_ratio_100g", "nutrition_score_fr_100g",
    "nutrition_score_uk_100g"
]

# Ensure usecols matches actual columns (ignoring case and spaces)
columns_to_keep = [col for col in columns_to_keep if col in actual_columns]

chunk_size = 100000  # Adjust the chunk size based on your memory capacity
chunks = []

# Process the file in chunks
try:
    for chunk in pd.read_csv('food_details.tsv', delimiter='\t', usecols=columns_to_keep, on_bad_lines='skip', chunksize=chunk_size, low_memory=False):
        chunks.append(chunk)
except ValueError as e:
    print(f"An error occurred: {e}")

# Concatenate all chunks
if chunks:
    df = pd.concat(chunks, ignore_index=True)

    # Remove rows with null values in specific columns
    columns_to_check = ["product_name", "energy_100g", "fat_100g"]
    df = df.dropna(subset=columns_to_check)

    # Display the DataFrame
    print(df.describe())
    print(df.head(5))

    # Save the cleaned data to a new file
    df.to_csv('cleaned_food_details.csv', index=False)
else:
    print("No data was processed.")

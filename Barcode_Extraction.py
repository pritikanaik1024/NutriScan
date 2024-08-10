import pandas as pd
df = pd.read_csv('Preprocessed_Nutritional_Dataset.csv')
# Define column types if known
dtype_spec = {
    'code': int,
    # 'ColumnA': float,
    # 'ColumnB': int,
}

# Load the dataset with specified data types
df = pd.read_csv('Preprocessed_Nutritional_Dataset.csv', dtype=dtype_spec, low_memory=False)

# Check if 'Barcode' column exists and extract it
if 'code' in df.columns:
    # Extract barcode column
    barcode_df = df[['code']]
    # Save the barcode data to a separate CSV file
    barcode_df.to_csv('Barcode_Data.csv', index=False)
    print("Barcode data saved successfully.")
else:
    print("Barcode column not found in the dataset.")

# Remove the barcode column from the original dataframe
df_cleaned = df.drop(columns=['code'], errors='ignore')

# Save the cleaned dataset
df_cleaned.to_csv('Cleaned_Dataset.csv', index=False)
print("Cleaned dataset saved successfully.")


# from PIL import Image
# import numpy as np
# import os
#
# def load_image(image_path):
#     with Image.open(image_path) as img:
#         img = img.convert('L')  # Convert to grayscale
#         img = img.resize((128, 128))  # Resize for consistency
#         return np.array(img)
#
#
# def load_labels(label_path):
#     with open(label_path, 'r') as file:
#         return file.read().strip()
#
#
# image_folder = 'dataset/images'
# label_folder = 'dataset/labels'
#
# images = []
# labels = []
#
# for image_file in os.listdir(image_folder):
#     image_path = os.path.join(image_folder, image_file)
#     label_file = image_file.replace('.jpg', '.txt')
#     label_path = os.path.join(label_folder, label_file)
#
#     if os.path.exists(label_path):
#         images.append(load_image(image_path))
#         labels.append(load_labels(label_path))
#
# # Convert lists to arrays
# X = np.array(images)
# y = np.array(labels)
#
# from PIL import Image
# import pytesseract
#
# # Path to the tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# # Perform OCR on an image
# def extract_text(image_path):
#     img = Image.open(image_path)
#     text = pytesseract.image_to_string(img)
#     return text
#
# # Example usage
# barcode_text = extract_text('path_to_image.jpg')
# print(f"Extracted text: {barcode_text}")

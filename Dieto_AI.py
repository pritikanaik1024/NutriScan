import pandas as pd
class DietoAI:
    def __init__(self, dataframe):
        self.df = dataframe
        # Ensure 'Recipe_name' is a string column
        self.df['Recipe_name'] = self.df['Recipe_name'].astype(str)
        # Create a mapping for diet types to numeric codes and vice versa
        self.diet_type_mapping = {diet: idx + 1 for idx, diet in enumerate(self.df['Diet_type'].unique())}
        self.diet_type_reverse_mapping = {v: k for k, v in self.diet_type_mapping.items()}

    def get_recipe_info(self, recipe_name):
        # Ensure 'Recipe_name' is a string column
        if self.df['Recipe_name'].dtype != 'object':
            self.df['Recipe_name'] = self.df['Recipe_name'].astype(str)
        # Convert to lowercase for comparison
        recipe_name = recipe_name.lower()
        recipe = self.df[self.df['Recipe_name'].str.lower() == recipe_name]
        if recipe.empty:
            return "Recipe not found."
        return recipe

    def generate_diet_plan(self, diet_type_name, min_protein, max_protein, min_carbs, max_carbs, min_fat, max_fat):
        # Convert diet_type_name to numeric code
        diet_type = self.diet_type_mapping.get(diet_type_name.lower(), None)
        if diet_type is None:
            return "Invalid diet type. Please provide a valid diet type."

        filtered_recipes = self.df[
            (self.df['Diet_type'] == diet_type) &
            (self.df['Protein(g)'] >= min_protein) &
            (self.df['Protein(g)'] <= max_protein) &
            (self.df['Carbs(g)'] >= min_carbs) &
            (self.df['Carbs(g)'] <= max_carbs) &
            (self.df['Fat(g)'] >= min_fat) &
            (self.df['Fat(g)'] <= max_fat)
            ]

        if filtered_recipes.empty:
            return "No recipes match the given criteria. Please adjust your preferences."

        n_samples = min(7, len(filtered_recipes))
        return filtered_recipes.sample(n=n_samples)

    def recommend_alternatives(self, protein_range, carbs_range, fat_range):
        alternatives = self.df[
            (self.df['Protein(g)'].between(*protein_range)) &
            (self.df['Carbs(g)'].between(*carbs_range)) &
            (self.df['Fat(g)'].between(*fat_range))
            ]

        if alternatives.empty:
            return "No alternatives found. Please adjust your criteria."

        return alternatives.sample(min(5, len(alternatives)))


def interactive_system():
    print("Welcome to Dieto_AI!")
    print(f"Available diet types: {', '.join(map(str, dieto_ai.diet_type_reverse_mapping.values()))}")

    while True:
        print("\nChoose an option:")
        print("1. Generate Diet Plan")
        print("2. Get Recipe Info")
        print("3. Recommend Alternatives")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            diet_type_name = input("Enter diet type: ")
            min_protein = float(input("Enter minimum protein (standardized): "))
            max_protein = float(input("Enter maximum protein (standardized): "))
            min_carbs = float(input("Enter minimum carbs (standardized): "))
            max_carbs = float(input("Enter maximum carbs (standardized): "))
            min_fat = float(input("Enter minimum fat (standardized): "))
            max_fat = float(input("Enter maximum fat (standardized): "))
            diet_plan = dieto_ai.generate_diet_plan(diet_type_name, min_protein, max_protein, min_carbs, max_carbs,
                                                    min_fat, max_fat)
            print(diet_plan)

        elif choice == '2':
            recipe_name = input("Enter recipe name: ")
            recipe_info = dieto_ai.get_recipe_info(recipe_name)
            print(recipe_info)

        elif choice == '3':
            min_protein = float(input("Enter minimum protein (standardized): "))
            max_protein = float(input("Enter maximum protein (standardized): "))
            min_carbs = float(input("Enter minimum carbs (standardized): "))
            max_carbs = float(input("Enter maximum carbs (standardized): "))
            min_fat = float(input("Enter minimum fat (standardized): "))
            max_fat = float(input("Enter maximum fat (standardized): "))
            alternatives = dieto_ai.recommend_alternatives((min_protein, max_protein), (min_carbs, max_carbs),
                                                           (min_fat, max_fat))
            print(alternatives)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Load the preprocessed dataset
df = pd.read_csv('Preprocessed_Diet_Dataset.csv')

# Initialize the DietoAI class
dieto_ai = DietoAI(df)

# Run the interactive system
interactive_system()
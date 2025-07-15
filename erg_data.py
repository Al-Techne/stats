import pandas as pd

# Load CSV file into a DataFrame
df = pd.read_csv('concept2-season-2025.csv')

# Show the entire DataFrame
print(df)

# Access the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

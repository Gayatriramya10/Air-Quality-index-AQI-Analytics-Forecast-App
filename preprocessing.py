import pandas as pd
# Load the dataset
df = pd.read_csv("data/city_day.csv")
# Display first 5 rows
print(df.head())
# Display dataset information
print(df.info())
# Check missing values
print(df.isnull().sum())
#check duplicate rows
print("Duplicate rows:",df.duplicated().sum())
# Handle missing values in pollutant columns

pollutant_cols = [
    'PM2.5', 'PM10', 'NO', 'NO2', 'NOx',
    'NH3', 'CO', 'SO2', 'O3',
    'Benzene', 'Toluene', 'Xylene'
]

for col in pollutant_cols:
    df[col] = df.groupby('City')[col].transform(
        lambda x: x.fillna(x.median())
    )

    # Fill any remaining missing values
    df[col] = df[col].fillna(df[col].median())

# Check remaining missing values
print("\nMissing values after handling:")
print(df.isnull().sum())
# Remove duplicate rows
df= df.drop_duplicates()

print("Duplicates after removal:", df.duplicated().sum())
# Convert Date column into datetime
df['Date'] = pd.to_datetime(df['Date'])

print("Date data type:", df['Date'].dtype)
# Save cleaned dataset
df.to_csv("data/clean_city_day.csv", index=False)

print("Cleaned dataset saved successfully!")
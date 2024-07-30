import pandas as pd

# Load the dataset
df = pd.read_excel('data/udemy1.xlsx')

# Display basic information about the dataset
print(df.info())
print(df.head())

# Print column names
print(df.columns)

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Convert date columns to datetime type (make sure to use the correct column name)
if 'published_timestamp' in df.columns:
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
else:
    print("Column 'published_timestamp' not found in the dataset.")
    print("Available columns:", df.columns)

# Check the data types again
print(df.dtypes)

# Save the cleaned dataset
df.to_csv('data/cleaned_udemy_courses.csv', index=False)

print("Data cleaning and preprocessing completed.")

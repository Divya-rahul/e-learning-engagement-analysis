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

# Convert date columns to datetime type
df['last_update'] = pd.to_datetime(df['last_update'])

# Check the data types again
print(df.dtypes)

# Save the cleaned dataset
df.to_csv('data/cleaned_udemy_courses.csv', index=False)

print("Data cleaning and preprocessing completed.")

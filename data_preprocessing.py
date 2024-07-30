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

# Drop the unnecessary 'Unnamed: 9' column if it exists
if 'Unnamed: 9' in df.columns:
    df = df.drop(columns=['Unnamed: 9'])

# Handle missing values
df = df.dropna(subset=['last_update'])  # Ensure date column has no missing values

# Convert date columns to datetime type
df['last_update'] = pd.to_datetime(df['last_update'])

# Fill missing values in other columns (if necessary)
df = df.fillna({
    'category': 'Unknown',
    'title': 'No Title',
    'short_decs': 'No Description',
    'rating': df['rating'].mean(),
    'student_num': '0',
    'points': '0',
    'creator': 'Unknown',
    'language': 'Unknown',
    'price': '0',
    'duration': '0',
    'long_desc': 'No Description'
})

# Ensure numerical columns are of correct type
df['rating'] = df['rating'].astype(float)
df['student_num'] = df['student_num'].str.replace(',', '').astype(int)
df['points'] = df['points'].str.replace(',', '').astype(int)
df['price'] = df['price'].str.replace(',', '').astype(float)
df['duration'] = df['duration'].str.replace(',', '').astype(float)

# Save the cleaned dataset
df.to_csv('data/cleaned_udemy_courses.csv', index=False)

print("Data cleaning and preprocessing completed.")

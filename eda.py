import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_udemy_courses.csv')

# Plot the distribution of course prices
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Distribution of Course Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('plots/course_price_distribution.png')
plt.show()

# Plot the number of courses published each year
df['year'] = pd.DatetimeIndex(df['published_timestamp']).year
plt.figure(figsize=(10, 6))
sns.countplot(x='year', data=df)
plt.title('Number of Courses Published Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Courses')
plt.xticks(rotation=45)
plt.savefig('plots/courses_per_year.png')
plt.show()

print("Exploratory Data Analysis completed.")

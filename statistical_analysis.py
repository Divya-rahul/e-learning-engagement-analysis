import pandas as pd
import scipy.stats as stats

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_udemy_courses.csv')

# Perform a correlation analysis between course price and number of subscribers
correlation, p_value = stats.pearsonr(df['price'], df['num_subscribers'])
print(f'Correlation between price and number of subscribers: {correlation:.2f}')
print(f'P-value: {p_value:.2e}')

# Perform a t-test between free and paid courses on number of subscribers
free_courses = df[df['is_paid'] == False]['num_subscribers']
paid_courses = df[df['is_paid'] == True]['num_subscribers']
t_stat, p_val = stats.ttest_ind(free_courses, paid_courses)
print(f'T-test between free and paid courses - T-statistic: {t_stat:.2f}, P-value: {p_val:.2e}')

print("Statistical Analysis completed.")

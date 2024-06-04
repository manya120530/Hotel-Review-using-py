import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df= pd.read_csv("Hotel_Reviews (1).csv" , sep=",")
print(df)

df.head()

# Find the number of rows and columns
rows, cols = df.shape

print(f"Number of rows: {rows}")
print(f"Number of columns: {cols}")

# Look for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values[missing_values > 0])

# Drop unnecessary columns
columns_to_drop = ['Tags', 'days_since_review', 'Additional_Number_of_Scoring']
df = df.drop(columns=columns_to_drop)
print(df.head())

# Check for duplicate rows
duplicate_rows = df[df.duplicated()]
print(f"\nNumber of duplicate rows: {duplicate_rows.shape[0]}")

# Display the duplicate rows if any
if duplicate_rows.shape[0] > 0:
    print("Duplicate rows:")
    print(duplicate_rows)

# Get descriptive statistics for numerical columns to find outliers
descriptive_stats = df.describe()
print("\nDescriptive statistics for numerical columns:")
print(descriptive_stats)

# Look for any anomalies in the dataset
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())


# Cleaning the data

# Remove duplicate rows
df = df.drop_duplicates()
print(df)

# Handle missing values
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col].fillna(df[col].median(), inplace=True)
    print(df)

# For categorical columns, you might choose to fill with a placeholder or mode
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna('Unknown', inplace=True)
    print(df)

# Creating a correlation heatmap
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap (Numerical Features)")
plt.show()

# Plotting the worst top 10 and best top 10 hotels according to reviewer score
top_10_worst_hotels = data.nsmallest(10, 'Reviewer_Score')
top_10_best_hotels = data.nlargest(10, 'Reviewer_Score')

plt.figure(figsize=(12, 6))

# Plotting worst 10 hotels
worst_hotels = df.sort_values(by='Reviewer_Score').head(10)
plt.figure(figsize=(11,4))
plt.bar(worst_hotels['Hotel_Name'], worst_hotels['Reviewer_Score'])
plt.xlabel('Hotel Name')
plt.ylabel('Reviewer Score (Worst)')
plt.title('Top 10 Worst Rated Hotels')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting best 10 hotels
best_hotel = df.sort_values(by='Reviewer_Score', ascending=False).head(1)
plt.figure(figsize=(6,4))
plt.bar(best_hotel['Hotel_Name'], best_hotel['Reviewer_Score'])
plt.xlabel('Hotel Name')
plt.ylabel('Reviewer Score (Best)')
plt.title('Top Rated Hotel')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

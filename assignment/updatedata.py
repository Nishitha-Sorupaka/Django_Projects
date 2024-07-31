#Updating CSV file data - Removing Empty fields and Replacing with random data from same column
import pandas as pd
import numpy as np
#load the CSV file
file_path = "E:\\Django_Projects\\assignment\\assignment movies.xlsx - Sheet1.csv"
df = pd.read_csv(file_path)

#Displaying the first few rows of the DataFrame
print("Original DataFrame:")
print(df.head())

#check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
print(df.dtypes)

#Handling missing values for numeric columns
df['RATING'].fillna(df['RATING'].mean(), inplace=True)
df['RunTime'].fillna(df['RunTime'].median(), inplace=True)

df['RATING'] = round(df['RATING'], 1)

#Function to fill NaN values with random non-NaN values from the same column
def fill_na_with_random(df):
    for column in df.columns:
        if df[column].dtype == object:  #Only to all object type columns
            non_na_values = df[column].dropna().unique()
            df[column] = df[column].apply(lambda x: np.random.choice(non_na_values) if pd.isna(x) else x)
    return df

# Function to replace values in 'MOVIES' column that start with a digit
def replace_numeric_start_in_column(df, column):
    # Create a boolean mask where the values start with a digit or are NaN
    mask = df[column].str[0].str.isdigit() | df[column].isnull()
    #mask = df[column].str[0].str.isdigit() | df[column].str[-1].str.isdigit() | df[column].isnull()
    # Identify non-numeric values in the column
    non_numeric_values = df.loc[~mask, column].unique()
    # Replace values starting with a digit with random non-numeric values
    replace_values = np.random.choice(non_numeric_values, size=mask.sum(), replace=True)
    df.loc[mask, column] = replace_values
    return df

# Replace numeric-starting values in 'MOVIES' column
df = replace_numeric_start_in_column(df, 'MOVIES')

# Fill NaN values in string columns
df = fill_na_with_random(df)


#Displaying the DataFrame after handling missing values
print("\nDataFrame after handling missing values:")
print(df.head())

#check for missing values again
print("\nMissing values in each column after handling missing values:")
print(df.isnull().sum())

# Save the cleaned DataFrame to a new CSV file (if needed)
cleaned_file_path = 'E:\\Django_Projects\\assignment\\cleaned_movies.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned data saved to {cleaned_file_path}")

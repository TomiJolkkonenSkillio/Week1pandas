import pandas as pd

# 1. Create a DataFrame with 3 columns, name, age, score. Create 5 random persons
data1 = {
    'Name': ['Jack', 'Alice', 'Steven', 'John', 'Emma'],
    'Age': [28, 28, 52, 40, 22],
    'Score': [9, 10, None, 8, None] # some missing values
}

df1 = pd.DataFrame(data1)

# 2. set name as index
df1.set_index('Name')

# 2. slice dataframe to display ages over 25
dfAgesOver25 = df1[df1['Age'] > 25]

# 3. convert score to float
dfAgesOver25['Score'].astype(float)

# 4. group the dataframe by the age column and calculate the mean score for each age group
df1.set_index('Age')

# 5. fill missing values
dfAgesOver25 = df1.fillna({'Score': df1['Score'].mean()})

# print results
# print((dfAgesOver25))

# 6. create another dataframe 3 columns name age occupation 5 persons
data2 = {
    'Name': ['Jill', 'William', 'Anders', 'Elin', 'Joakim'],
    'Age': [34, 34, 34, 40, 22],
    'Score': [9, 10, 6, 8, 6]
}

df2 = pd.DataFrame(data2)

# 6. concatenate 2 sets together
concatenated_df = pd.concat([df1, df2], ignore_index=True)
# print(concatenated_df)

# 7. create 2 dataframes, id and name, and id occupation and salary
# use merge to merge them together based on id column

data3 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Jill', 'William', 'Anders', 'Elin', 'Joakim'],
    'Age': [34, 34, 34, 40, 22]

}

data4 = {
    'ID': [1, 2, 3, 4, 5],
    'Occupation': ['Student', 'Rock star', 'Movie star', 'Hockey star', 'Star']
}

df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)

merged_df = pd.merge(df3, df4, on='ID', how='inner')
# print(merged_df)

# 8. create dataframe with date column, date strings in yyyy-mm-dd, use datetime to convert it to datetime format

data5 = {
    'Date': ['2020-08-01', '2020-08-01', '2020-08-01', '2020-08-01', '2020-08-01'],
    'Random': ['ran', 'rand', 'ando', 'ndom', 'and']
}

df5 = pd.DataFrame(data5)
df5['Date'] = pd.to_datetime(df5['Date'])
# print(df5)


# 9. rename columns in dataframe to EventDate and EventValue for another chosen columb
df5 = df5.rename(columns={'Date': 'EventDate', 'Random': 'EventValue'})
# print(df5)

# 10. create daraframe, column containing repetitive values, use unique to display vunique values in that columns

data6 = {
    'Age': [34, 34, 34, 40, 22]

}

df6 = pd.DataFrame(data6)
unique_values = df6['Age'].unique()
print(unique_values)

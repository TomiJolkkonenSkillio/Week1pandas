import pandas as pd

# 1. download and the file
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

# 2. rename colmuns not to have whitespace or special characters
df.columns = df.columns.str.replace(" ", "").str.replace("[^\w]", "", regex=True)

# 3. persons under 18, set sex to child
dfUnder18 = df[df['Age'] < 18]
dfUnder18.replace({'Sex': {'male': 'Child'}, }, inplace=True)
dfUnder18.replace({'Sex': {'female': 'Child'}, }, inplace=True)

print("first few rows of the DataFrame:")
# print(dfUnder18.head())

# Step 4: Create a new dataset displaying the average fare per sex
df2 = pd.read_csv(file_path)
df2 = df2.groupby('Sex')['Fare'].mean().reset_index()
print("Dataset with average fare per sex:")
print(df2)

# Step 5: Create a new dataset displaying the average fare per sex and Pclass
df3 = pd.read_csv(file_path)
df3 = df3.groupby(['Sex', 'Pclass'])['Fare'].mean().reset_index()
print("\nDataset with average fare per sex and Pclass:")
print(df3)

# Step 6: Create a new dataset displaying the average fare per survived column
df4 = pd.read_csv(file_path)
df4 = df4.groupby('Survived')['Fare'].mean().reset_index()
print("\nDataset with average fare per survived column:")
print(df4)

# 7. split dataset into 3 datasets based on sex column (male, female, child), how many records does each dataset have?


# 8. new dataset, onlu Pclass name and age, for those who have siblings, spouces, parents, children aboard


# 9. filter off persons who had both siblings/spouses and parents/children


# 10. average fare paid by the people in the last dataset?


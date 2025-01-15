import pandas as pd

# 1. download and the file
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

# 2. rename colmuns not to have whitespace or special characters
df.columns = df.columns.str.replace(" ", "").str.replace("[^\w]", "", regex=True)

# 3. persons under 18, set sex to child
df[df['Age'] < 18]
df.replace({'Sex': {'male': 'Child'}, }, inplace=True)
df.replace({'Sex': {'female': 'Child'}, }, inplace=True)

print("first few rows of the DataFrame:")
print(df.head())

# Step 4: Create a new dataset displaying the average fare per sex
df2 = pd.read_csv(file_path)
df2_avrFarePerSex = df2.groupby('Sex')['Fare'].mean().reset_index()

# Step 5: Create a new dataset displaying the average fare per sex and Pclass
df3 = pd.read_csv(file_path)
dfAvrFarePerSexAndClass = df3.groupby(['Sex', 'Pclass'])['Fare'].mean().reset_index()

# Step 6: Create a new dataset displaying the average fare per survived column
df4 = pd.read_csv(file_path)
dfAvrFarePerSurvivor = df4.groupby('Survived')['Fare'].mean().reset_index()

# 7. split dataset into 3 datasets based on sex column (male, female, child), how many records does each dataset have?
df8 = pd.read_csv(file_path)
male_df = df8[df8['Sex'] == 'male']
female_df = df8[df8['Sex'] == 'female']
child_df = df8[df8['Sex'] == 'child']
male_count = male_df.shape[0]
female_count = female_df.shape[0]
child_count = child_df.shape[0]

# 8. new dataset, only Pclass name and age, for those who have siblings, spouces, parents, children aboard
df5 = pd.read_csv(file_path)
family_aboard = (df5['Siblings/Spouses Aboard'] > 0) | (df5['Parents/Children Aboard'] > 0)
passengers_with_family = df5.loc[family_aboard, ['Pclass', 'Age']]

# 9. filter off persons who had both siblings/spouses and parents/children
df6 = pd.read_csv(file_path)
df6_filtered = df6[(df6['Siblings/Spouses Aboard'] > 0) & (df6['Parents/Children Aboard'] > 0)]

# 10. average fare paid by the people in the last dataset?
df7 = pd.read_csv(file_path)
dfAvrFareLast = df7['Fare'].mean()



def main():
    print(f"Average Fare per Sex:\n{df2_avrFarePerSex}\n")
    print(f"Average Fare per Sex and Pclass:\n{dfAvrFarePerSexAndClass}\n")
    print(f"Average Fare per Survived:\n{dfAvrFarePerSurvivor}\n")
    print(f"Record counts - Male: {male_count}, Female: {female_count}, Child: {child_count}\n")
    print(f"Those who have siblings, spouses, parents or children aboard: {passengers_with_family}")
    print(f"Filtered off those who had both siblings/spouses and parents/children: {df6_filtered}")
    print(f"Average fare paid by the people in the previous dataset: {dfAvrFareLast}")

if __name__ == "__main__":
    main()
import pandas as pd
data = {
    'Name': ['Anu', 'Binu', 'Cathy', 'David', 'Esha'],
    'Age': [20, 25, 22, 30, 24],
    'Marks': [85, 72, 90, 65, 88],
    'City': ['Kochi', 'Calicut', 'Kochi', 'Kannur', 'Calicut']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

result1 = df.loc[df['Marks'] > 80]
print("\nStudents with marks greater than 80:")
print(result1)

result2 = df.loc[df['Age'] >= 24]
print("\nStudents aged 24 or above:")
print(result2)

result3 = df.loc[(df['City'] == 'Kochi') & (df['Marks'] > 80)]
print("\nStudents from Kochi with marks > 80:")
print(result3)

result4 = df.loc[df['Marks'] > 80, ['Name', 'Marks']]
print("\nName and Marks of students with marks > 80:")
print(result4)
import pandas as pd
data = {
    'Name': ['Anu', 'Ammu', 'Meera', 'Athira', ],
    'Age': [20, 21, 19, 22, ],
    'Mark': [85, 90, 78, 88, ],
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())
print("\nBasic Information:")
print(df.info())
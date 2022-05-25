import pandas as pd

d = {'one': [1, 1, 1, 1, 1], 'two': [2, 2, 2, 2, 2], 'letter': ['a', 'a', 'b', 'b', 'c']}
df = pd.DataFrame(d)
print(df)

df1 = df.groupby('letter')
print(df1)
print(df1.head())

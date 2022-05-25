import pandas as pd

d = {'a': [1, 1, 1, 1], 'b': [2, 2, 2, 2], 'c': [3, 3, 3, 3]}
i = ['w1', 'w2', 'w3', 'w4']
df = pd.DataFrame(data=d, index=i)

print(df)

print(df.loc['w1'])
print(df.loc['w1':'w3'])
print(df.loc['w1', 'a'])

print(df.iloc[0, 0])
print(df.iloc[0:2, 0])
print(df.loc['w2', 'b'])
print(df.iloc[1, 1])
print(df['b'])
print(df.loc[:, 'b'])

print(df.describe())

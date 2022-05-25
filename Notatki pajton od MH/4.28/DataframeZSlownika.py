import pandas as pd

d = {'one': [1, 1], 'two': [2, 2]}
i = ['a', 'b']
df = pd.DataFrame(data=d, index=i)
print(df)

print(df.columns)
print(df.index)

df.columns = ['pierwsza', 'druga']
print(df)

df.index = ['w1', 'w2']
print(df)

print(df['pierwsza'])
print(df['druga'])

df['trzecia'] = 5
print(df)

df['czwarta'] = df['trzecia'] + 1
print(df)

del df['czwarta']
print(df)

df.drop('w2')       # Nie zmienia df, trzeba uzyc
print(df)           #
df = df.drop('w2')  # df = dr.drop('')
print(df)

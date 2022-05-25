import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

df.at[dates[0], 'A'] = 0
print(df)

df.at[dates[3], 'C'] = 100
print(df)

df.at[dates[2], 'B'] = 50
print(df)

stack = df.stack()
print(stack)
print(stack.index)

unstack = df.unstack()
print(unstack)

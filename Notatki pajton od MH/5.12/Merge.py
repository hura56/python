import pandas as pd

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})  # ramka 1
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})  # ramka 2

print(pd.merge(left, right, on='key1'))
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))
print(pd.merge(left, right, on=['key1', 'key2']))
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))

zip([1, 2], ['a', 'b', 'c'])
list(zip([1, 2], ['a', 'b', 'c']))

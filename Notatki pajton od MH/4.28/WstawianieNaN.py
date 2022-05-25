import numpy as np
import pandas as pd

df = pd.DataFrame([x for x in range(10)])
print(df)
print(df.replace(2, np.nan))
print(df.replace({9: 100, 5: np.NaN}))
df = df.replace(2, np.nan)
print(df)

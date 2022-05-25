import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Initial preparation

# read data
df = pd.read_excel('Data.xls', sheet_name='Data')
# df = pd.read_csv('Data.csv')
print(df)

# data head
print(df.head())

# columns
print("Column headings:")
print(df.columns)

# indices for columns
dfcolumns = {name: nr for nr, name in enumerate(df.columns)}

print(df.loc[:, 'M1':'M4'])

# checking uniquenes
print(sorted(df.iloc[:, dfcolumns['M2']].unique()))

# indices for M-columns. We remove some that are not good for decribe
# imSelected=[i for i in range(dfcolumns['M1'],dfcolumns['M4']) if (i != dfcolumns['M2']) and (i != dfcolumns['M3']) ]; print(imSelected)
imSelected = [i for i in range(dfcolumns['M1'], dfcolumns['M4']+1)]
mSelected = df.iloc[:, imSelected].copy()
print(mSelected.columns)
print(mSelected.head())

# select p columns
pSelected = df.loc[:, 'P1.1':'P2.18'].copy()
print(pSelected.columns)

# 1.1) Transforming data

# dictionary abc -> 123
translateDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# and inverse transform
inv_translateDict = {v: k for k, v in translateDict.items()}
mSelected.loc[:, "M1":"M4"] = mSelected.loc[:, "M1":"M4"].applymap(lambda x: translateDict[x])
print(mSelected.head())

# 1.2) Removing NaN

# check unique values
print(sorted(mSelected.loc[:, 'M1'].unique()))

# Checking NaN
mSelected.isnull().any()
# mSelected.isnull().any()
print(mSelected.isnull().sum())

# Checking NaN
pSelected.isnull().values.any()
# pSelected.isnull().any()
print(pSelected.isnull().sum())

# Data is very clean. We remove NaN by replacing with zero.

# removing NaN
mSelected.fillna(0, inplace=True)
pSelected.fillna(0, inplace=True)

# Chekcing NaN
print(pSelected.isnull().values.any())

# Checking NaN
print(mSelected.isnull().values.any())

# 2) Correlation analysis
# 2.0.1) Definitions


def cov_matrix(m):
    """Plot covariance matrix and returns it"""
    print(m.columns)
    cov_data = np.corrcoef(m.T)
    # print(cov_data)
    plt.figure(figsize=(20, 20))
    # plt.yticks(range(np.shape(cov_data)[1]),metryczkiSelected.columns[::-1])
    # plt.xticks(range(np.shape(cov_data)[1]),metryczkiSelected.columns)
    # img = plt.matshow(cov_data, cmap=plt.cm.rainbow, fignum = 1)
    # plt.colorbar(img,ticks=[-1,0,1],fraction = 0.045)
    # for x in range(cov_data.shape[0]):
    # for y in range(cov_data.shape[1]):
    # plt.text(x,y,"%0.2f" % cov_data[x,y], size=12, color='black', ha="center", va="center" )
    sns.heatmap(cov_data, cbar=True, annot=True, square=True, annot_kws={'size': 15}, fmt='.2f', xticklabels=m.columns, yticklabels=m.columns)
    return cov_data

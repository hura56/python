import os
import pandas as pd

"""
Formaty plikow
    df.to_csv('plik.csv', index=False)
    df.to_excel('plik.xls', index=False)
    df.to_csv('plik.txt', index=False)
"""
d = {'one': [1, 1, 1, 1, 1], 'two': [2, 2, 2, 2, 2], 'letter': ['a', 'a', 'b', 'b', 'c']}
df = pd.DataFrame(d)

print(os.getcwd())
df.to_csv('plik.txt', index=False)

FileNames = []
os.chdir('.')       # . to current directory
for files in os.listdir('.'):
    if files.endswith(".txt"):
        FileNames.append(files)


print(FileNames)

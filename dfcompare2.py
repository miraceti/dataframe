import pandas as pd
import numpy as np
import datacompy

# depuis des fichiers csv ou xlsx
df1 = pd.read_excel("fichier1.xlsx", sheet_name="DATA")
df2 = pd.read_excel("fichier2.xlsx", sheet_name="DATA")
print(df1)
print(df2)

dif = df1.melt()
print(dif)
dif.columns=['Columns', 'Before']
dif.insert(2, 'After', df2.melt().value)
dif2 = dif[dif.Before!=dif.After]

print(dif2)
import pandas as pd
import numpy as np
import datacompy

# depuis des fichiers csv ou xlsx
df1 = pd.read_excel("fichier1.xlsx", sheet_name="DATA")
df2 = pd.read_excel("fichier2.xlsx", sheet_name="DATA")
print(df1)
print(df2)

dif = []

for col in df1.columns:
    for bef,aft in zip(df1[col], df2[col]):
        if bef != aft :
            dif.append([col, bef, aft])
            
print(dif)
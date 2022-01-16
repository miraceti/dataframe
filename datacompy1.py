import pandas as pd
import numpy as np
import datacompy

# depuis des fichiers csv ou xlsx
df1 = pd.read_excel("fichier1.xlsx", sheet_name="DATA")
df2 = pd.read_excel("fichier2.xlsx", sheet_name="DATA")
print(df1)
print(df2)

# comparaison plusieurs colonnes commune avec changement de nom (avant apres)
comparison = datacompy.Compare(df1, df2, join_columns=["client_id","ordre_contrat"], df1_name="AVANT_MAJ", df2_name="APRES_MAJ")
print(comparison)

print('REPORT4')
print(comparison.report())

with open('report4.txt', 'w') as f:
    f.write(comparison.report())

print(comparison.df2_unq_rows)
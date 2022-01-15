import pandas as pd
import numpy as np
import datacompy

# depuis des fichiers csv ou xlsx
# df1 = pd.read_excel("fichier1.xlsx", sheet_name=2)
# df2 = pd.read_excel("fichier2.xlsx", sheet_name=2)

# ou avec dist ou list de list  dict : {"c1":["r1","r2","r3"], "c2":[11,12,13], "c3":[True,False,True]}
d1 =[["a",1,1,111],["b",2,2,112],["c",3,3,113],["d",4,4,114],["e",4,4,114],["f",4,4,114],["g",4,4,114]]
df1 =pd.DataFrame(d1, columns=["nom","pclid","pocid","cc_pla_gest_id"])
print(df1)
d2 =[["a",1,1,121],["b",2,2,112],["c",3,3,123],["d",4,4,114],["e",4,4,114],["f",4,4,118],["g",4,4,1194]]
df2 =pd.DataFrame(d2, columns=["nom","pclid","pocid","cc_pla_gest_id"])
print(df2)

# comparaison 1 colonne commune
comparison = datacompy.Compare(df1, df2, join_columns="nom")
print(comparison)

print('REPORT')
print(comparison.report())

with open('report.txt', 'w') as f:
    f.write(comparison.report())


# comparaison plusieurs colonnes commune
comparison2 = datacompy.Compare(df1, df2, join_columns=["nom","pclid"])
print(comparison2)

print('REPORT2')
print(comparison2.report())

with open('report2.txt', 'w') as f:
    f.write(comparison2.report())
    

# comparaison plusieurs colonnes commune avec changement de nom (avant apres)
comparison3 = datacompy.Compare(df1, df2, join_columns=["nom","pclid"], df1_name="AVANT_MAJ", df2_name="APRES_MAJ")
print(comparison3)

print('REPORT3')
print(comparison3.report())

with open('report3.txt', 'w') as f:
    f.write(comparison3.report())
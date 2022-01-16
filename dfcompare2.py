import pandas as pd

# depuis des fichiers csv ou xlsx 
df1 = pd.read_excel("fichier1.xlsx", sheet_name="DATA")
df2 = pd.read_excel("fichier2.xlsx", sheet_name="DATA")

def difference(df1,df2):
    dif = df1.melt()
    dif.columns=['Columns', 'Before']
    dif.insert(2, 'After', df2.melt().value)
    difference_df = dif[dif.Before!=dif.After]
    return(difference_df)

print(difference(df1,df2))
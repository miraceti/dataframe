import pandas as pd
import numpy as np
d1 = [["a",0,0,"000"],["b",1,1,"111"],["c",2,2,"222"],["d",3,3,"333"],["e",4,4,"444"],["f",5,5,"555"],["g",6,6,"666"]]
df1=pd.DataFrame(d1, columns=["nom","pid","cid","pass"])
print(df1)

d2 = [["a","000"],["b","111"],["c","222222"],["d","333"],["e","444444"],["f","555"],["g","666"]]
df2=pd.DataFrame(d2, columns=["nom","pass"])
print(df2)

print("\n DF11  on ne garde que les lignes identiques ")
df11 = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] == 'both']
print(df11)

print("\n DF12 on ne garde que les colonnes du xls cible")
df12 = df11[['nom','pid','cid','pass']]
print(df12)
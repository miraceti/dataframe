import pandas as pd
import numpy as np
print("\n DF1")
d1 = [["a",0,0,"000"],["b",1,1,"111"],["c",2,2,"222"],["d",3,3,"333"],["e",4,4,"444"],["f",5,5,"555"],["g",6,6,"666"]]
df1=pd.DataFrame(d1, columns=["nom","pid","cid","pass"])
print(df1)

print("\nDF2")
d2 = [["a","000"],["b","111"],["c","222222"],["d","333"],["e","444444"],["f","555"],["g","666"]]
df2=pd.DataFrame(d2, columns=["nom","pass"])
print(df2)

#############################################################################################
# on compare 2 df sur une colonne differente presente dans les 2 df
print("\n DF11  on ne garde que les lignes identiques :both ")
df11 = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] == 'both']
print(df11)

print("\n DF12 on exclu les colonnes 'both' pour ajout des autres colonnes au xls cible")
df12 = df11[['nom','pid','cid','pass']]
print(df12)


#############################################################################################
print("\n DF3   df3 a exclure de DF1")
# on compare 2 df sur une condition de présence de valeur dans le second : df3 sert de filtre
d3 = [["b"],["d"],["g"]]
df3=pd.DataFrame(d3, columns=["nom"])
print(df3)

print("\n DF30  on compare df1 et df3 pour taguer les 'both' on eliminera les both ensuite")
# difference ente df1 et df3 method2: both <=> valeur présente dans 2 df et donc a elimner
df30 = df1.merge(df3, indicator=True, how='outer')
print("\ndf30")
print(df30)

# on compare 2 df sur une  presence dans le second de valeur
print("\n DF31  on ne garde que les lignes presente dans le df1 et pas dans le df3 (eliminaion des 'both') ")
df31 = df1.merge(df3, indicator=True, how='outer').loc[lambda v: v['_merge'] != 'both']
print(df31)

print("\n DF32 on ne garde que les colonnes du df1 filtre pour ajout au xls cible")
df32 = df31[['nom','pid','cid','pass']]
print(df32)

#############################################################################################
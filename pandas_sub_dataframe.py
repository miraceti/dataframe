import pandas as pd
import numpy as np

# exemple de ligne par c1,c2,c3,c4,c5,c6,c7,c8,c9,c10
# pour c1 on a 8 lignes 
# on a laes mêmes colonnes

# exemple de dataframe depuis une liste basique 
#liste de colonnes
liste1 =[["c1",11,21,31,41],["c1",12,22,32,42],["c1",13,23,33,43],["c1",14,24,34,44],
         ["c1",15,25,35,45],["c1",16,26,36,46],["c1",17,27,37,47],["c1",18,28,38,48],
         ["c2",11,21,31,41],["c2",12,22,32,42],["c2",13,23,33,43],["c2",14,24,34,44],
         ["c2",15,25,35,45],["c2",16,26,36,46],["c2",17,27,37,47],["c2",18,28,38,48],
         ["c3",11,21,31,41],["c3",12,22,32,42],["c3",13,23,33,43],["c3",14,24,34,44],
         ["c3",15,25,35,45],["c3",16,26,36,46],["c3",17,27,37,47],["c3",18,28,38,48],
         
         ]
print(liste1)
df1 =pd.DataFrame(liste1, columns=["contrat","m1","m2","m3","m4"])
print("\nDF1\n",df1)

# un dataframe avec nom de colonne et sans index"
df2 =  df1.set_index('contrat')
print("\nDF2\n",df2)

#creation de sous dataframe suivant critère
contrat = str("c1")
df31 = df1[df1["contrat"]==str(contrat)]
print("\nDF31\n",df31)

contrat = str("c2")
df32 = df1[df1["contrat"]==str(contrat)]
print("\nDF31\n",df32)

contrat = str("c3")
df33 = df1[df1["contrat"]==str(contrat)]
print("\nDF31\n",df33)

#creation d'une colonne qui somme  2 colonnes
# liste des colonnes a sommer
listecol1 = ["m1","m3"]

# nouvelle colonne avec la somme  : la fonction "copy()"recopie le dataframe dans un nouveu sinon les 2 sont identique si on fait "="
df311 = df31.copy()
df311['sum_m1_m3']= df311[listecol1].sum(axis=1)
print("\nDF311\n",df311)

print("\nDF31\n",df31)# df31 est inchangé alors qu'il l'aurait été si on avait fait df311 = df31 au lieu de df311 = df31.copy()

# group by 
df11 = df1.copy()
df11.groupby('contrat')[["m2","m4"]].sum()
print("\nDF11a\n",df11)

df11.iloc[:,[2,4]]=df11.iloc[:,[2,4]]*0.001
print("\nDF11b\n",df11)

#concatener 2 dataframes : 2 cas 
#1:cote a cote
dfhorizontal = pd.concat([df31,df32], axis = 1)
print("\ndfhorizontal\n",dfhorizontal)
#2:l'un en dessous de l'autre
dfvertical = pd.concat([df31,df32], axis = 0)
print("\ndfvertical\n",dfvertical)



# apliquer une fonction a une colonne d'un dataframe
modifieddataframe1 = df1.copy()
modifieddataframe1 = df1.apply(lambda x: np.square(x) if x.name =='m3' else x)
print("\nmodifieddataframe1\n",modifieddataframe1)

#autre solution : appliquer la function a une colonne et reassigner cette colonne au dataframe
modifieddataframe2 = df1.copy()
modifieddataframe2['m2'] = modifieddataframe2['m2'].apply(np.square)
print("\nmodifieddataframe2\n",modifieddataframe2)

#appliquer une fonction a une seule ligne du datframe
modifieddataframe3 = df2.copy()
modifieddataframe3b = modifieddataframe3.apply(lambda x: np.square(x) if x.name =='c2' else x, axis = 1)
print("\nmodifieddataframe3b\n",modifieddataframe3b)

#appliquer une fonction a plusieurs colonnes
modifieddataframe4 = df1.copy()
modifieddataframe4b = modifieddataframe4.apply(lambda x: np.square(x) if x.name in ['m1','m2'] else x)
print("\nmodifieddataframe4b\n",modifieddataframe4b)

#appliquer une fonction a plusieurs lignes
modifieddataframe5 = df2.copy()
modifieddataframe5b = modifieddataframe5.apply(lambda x: np.square(x) if x.name in ['c1','c3'] else x , axis=1)
print("\nmodifieddataframe5b\n",modifieddataframe5b)

#replace the NaN values in dataframe dfhorizontal
newdfhorizontal = dfhorizontal.fillna(value=0)
print("\nnewdfhorizontal\n",newdfhorizontal)

#replace the NaN values in dataframe dfhorizontal colonne
newdfhorizontalb = dfhorizontal.copy()
newdfhorizontalb['contrat'] = newdfhorizontalb['contrat'].fillna(value='cx')
print("\nnewdfhorizontalb\n",newdfhorizontalb)

#2 traitement de colonnes text ou nombre
newdfhorizontalc = dfhorizontal.copy()
newdfhorizontalc['contrat'] = newdfhorizontalc['contrat'].fillna(value='cx')
print("\nnewdfhorizontalc\n",newdfhorizontalc)
newdfhorizontalc = newdfhorizontalc.fillna(value=0)
print("\nnewdfhorizontalc\n",newdfhorizontalc)


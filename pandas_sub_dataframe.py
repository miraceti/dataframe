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

#dataframe depuis liste de tuples
employees =[(1,'a',10,'aa',11),
            (2,'a',20,'aa',21),
            (3,'a',30,'aa',31),
            (4,'a',40,'aa',41)]
df4 = pd.DataFrame(employees,
                   columns=['id','nom','age','city','experience'],
                   index=['e1','e2','e3','e4'])
print("\ndf4\n",df4)

#rowlabel
print(df4.index)
print(df4.index[2])

#columnames
print(df4.columns)
print(df4.columns[2])

#transposition du dataframe
df4_transpose = df4.T
print("\ndf4_transpose\n",df4_transpose)

#fataframe from dict
employees = {'nom':['a','b','c','d'],
               'age':[10,20,30,40],
               'city':['aa','bb','cc','dd'],
               'experience':[11,21,31,41]}
dfemployees = pd.DataFrame(employees)
print("\ndfemployees\n",dfemployees)


#sub df
subsetdf4a = df4.loc[lambda x : (x['age'] > 20).tolist()]
print("\nsubsetdf4a\n",subsetdf4a)

subsetdf4b = df4.loc[:,['age','city','nom']]
print("\nsubsetdf4b\n",subsetdf4b)

#select a cellvalue
cellvalue = df4.loc['e4','age'] # [ligne,colonne]
print(cellvalue)

subsetdf4c = df4.loc[['e1','e3'],['city','age']]
print("\nsubsetdf4c\n",subsetdf4c)

#mise à 0  du'une ligne
subsetdf4d = df4.copy()
subsetdf4d.loc['e3']=0
print("\nsubsetdf4d\n",subsetdf4d)


#appliquer une fonction a un dataframe
# methode 1
df5 = df4.copy()
print("\ndf5\n",df5)
df5['age'] = df5['age'].apply(lambda x: x+1)
print("\ndf5a\n",df5)

# methode 2
def addone(v):
    v += 1
    return v

df5b = df4.copy()
df5b['age'] = df5b.apply(lambda x: addone(x.age), axis=1)
print("\ndf5b\n",df5b)

# methode 3
df5c = df4.copy()
df5c['age'] = df5c['age'].map(addone)
print("\ndf5c\n",df5c)

# methode 4
df5d = df4.copy()
df5d['age'] = df5d['age'].map(lambda x: x + 1)
print("\ndf5d\n",df5d)

# methode 5 plusieurs colonnes
df5e = df4.copy()
df5e[['age','experience']] = df5e[['age','experience']].apply(lambda x: x + 1)
print("\ndf5e\n",df5e)

# methode 6
df5f = df4.copy()
df5f['age'] = df5f['age'].apply(addone)
print("\ndf5f\n",df5f)

# group by une colonne
df6 = df1.copy()
df6 =  df6.set_index('contrat')
print("\nDF6a\n",df6)
df6a = df6.groupby('contrat').agg(
             m1_sum = ('m1', 'sum'),
             m2_sum = ('m2', 'sum'),
             m3_count = ('m3', 'count'),
             m4_dif = ('m4', 'count'))
print("\nDF6a\n",df6a)

# To fill NaN with 0 use df['diff'].fillna(0, inplace=True)
# df['diff'] = df.groupby(['site', 'country'])['score'].diff().fillna(0)
df6b = df1.copy()
df6b =  df6b.set_index('contrat')
print("\nDF6b\n",df6b)

df6b['diff'] = df6b['m4']-df6b['m2']

print("\nDF6b\n",df6b)

# creation d'un dataframe aleatoire
df7 = pd.DataFrame(np.random.rand(100,5), columns=('a','b','c','d','e'))
print("\nDF7\n",df7)

#exemple de condition de comparaison avec la valeur 0.5 de la colonne a et création d'une colonne newcol avec b ou c
# df7.loc[np.logical_and(df7['a'].gt(0.5), np.less_equal(df7['b'],0.5)),'newcol'] = df7['b']
df7.loc[np.less_equal(df7['a'],0.5),'newcol'] = df7['b']
df7.loc[df7['a'].gt(0.5),'newcol'] = df7['c']
df7['newcol'].fillna('0.0', inplace=True)        
        
print("\nDF7a\n",df7)


# change value by where
df6c = df1.copy()
# df6c =  df6c.set_index('contrat')
print("\nDF6ca\n",df6c)
# print(df6c.loc[index,"m1"])

df6c.loc[df6c.m1 > 15,'diff2'] = 2
df6c.loc[df6c.m1 <= 15,'diff2'] = 1

print("\nDF6cb\n",df6c)

df6d = df6c.copy()
# df6d =  df6d.set_index('contrat')
print("\nDF6da\n",df6d)
# print(df6c.loc[index,"m1"])

df6d.loc[(df6d.contrat == 'c1') & (df6d.m2 > 25),'diff3'] = 2
df6d.loc[(df6d.contrat == 'c1') & (df6d.m2 <= 25),'diff3'] = 1
df6d.loc[(df6d.contrat != 'c1') , 'diff3'] = 0

print("\nDF6db\n",df6d)
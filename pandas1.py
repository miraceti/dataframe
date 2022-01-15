import pandas as pd
import numpy as np
d1 =[["a",1,1,111],["b",2,2,112],["c",3,3,113],["d",4,4,114],["e",4,4,114],["f",4,4,114],["g",4,4,114]]
df1 =pd.DataFrame(d1, columns=["nom","pclid","pocid","cc_pla_gest_id"])
print(df1)
d2 =[["a",1,1,121],["b",2,2,112],["c",3,3,123],["d",4,4,114],["e",4,4,114],["f",4,4,118],["g",4,4,1194]]
df2 =pd.DataFrame(d2, columns=["nom","pclid","pocid","cc_pla_gest_id"])
print(df2)

df3 = pd.concat([df1,df2],ignore_index='True').drop_duplicates(keep=False)
print(df3)

df4 = pd.merge(df1,df2,on='cc_pla_gest_id')
print(df4)

print(df1.equals(df2))

compare12 = df1.values == df2.values
print(compare12)

df7 = pd.concat([df1.set_index('nom'),df2.set_index('nom')], axis='columns', keys=['avant','après'])
df8 = df7.swaplevel(axis='columns')[df1.columns[1:]]

print(df7)
print(50*'*')
print(df8)

def hightlight(data, color='yellow'):
    attr = 'background-color: {}'.format(color)
    other = data.xs('avant', axis='columns', level=1)
    return pd.DataFrame(np.where(data.ne(other, level=0), attr, ''), index=data.index, columns=data.columns)

#df8.style.apply(hightlight, axis=None)
df8.style.apply(hightlight, axis=None).to_excel('resultdf8.xlsx', engine='openpyxl')

print("df10 a**************************")
df10 =pd.DataFrame(d1, columns=["nom","pclid","pocid","cc_pla_gest_id"])
print(df10)
print("df10 b")
df10 = df10.set_index('nom')
print(df10)

print('df9')
df9 = df1[['nom','pocid','cc_pla_gest_id']]
print(df9)

print('df11')
df11 = df9.set_index('nom')
print(df11)

#pour afficher  des lignes spécisfique  == .loc   df.loc[[listrowslabel],[listcolslabel]]
print("loc")
print(df11.loc[['a','c'],])
print(df11.loc[['a','c'],['cc_pla_gest_id']])
print(df11.loc[:,['cc_pla_gest_id']])

#pour afcicher par index                 ==.iloc   df.iloc[[listrowindex],[listcolumnindex]]
print("iloc")
print(df9.iloc[[1,3],[0,2]])
print(df11.iloc[:df11.index.get_loc('b'),:3])
print(df11.iloc[:df11.index.get_loc('b')+1,:3])


#difference entre df1 et df2 method1:
result12 = df1[~df1.apply(tuple,1).isin(df2.apply(tuple,1))]
print("result12")
print(result12)

# difference ente df1 et df2 method2:
df13 = df1.merge(df2, indicator=True, how='outer')
print("df13")
print(df13)

df14 = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] != 'both']
print("df14")
print(df14)

df15 = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] == 'right_only']
print("df15")
print(df15)

df16 = df1.merge(right=df2,
                 left_on = df1.columns.to_list(),
                 right_on = df2.columns.to_list(),
                 how = 'outer')
print("df16")
print(df16)

# rename columnname df1 et df2
df17 = df1.rename(columns = lambda x : x + '_file1')
df18 = df2.rename(columns = lambda x : x + '_file2')
print("df17")
print(df17)
print("df18")
print(df18)

df19 = df17.merge(right=df18,
                 left_on = df17.columns.to_list(),
                 right_on = df18.columns.to_list(),
                 how = 'outer')

print("df19")
print(df19)

records_in_df17_notin_df18 = df19.loc[df19[df18.columns.to_list()].isnull().all(axis=1),df17.columns.to_list()]
df20 = records_in_df17_notin_df18
print("df20")
print(df20)


records_in_df18_notin_df17 = df19.loc[df19[df17.columns.to_list()].isnull().all(axis=1),df18.columns.to_list()]
df21 = records_in_df18_notin_df17
print("df21")
print(df21)
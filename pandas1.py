import pandas as pd
import numpy as np
d1 =[["a",1,1,111],["b",2,2,112],["c",3,3,113],["d",4,4,114]]
df1 =pd.DataFrame(d1, columns=["nom","pclid","pocid","cc_pla_gest_id"])
print(df1)
d2 =[["a",1,1,121],["b",2,2,112],["c",3,3,123],["d",4,4,114]]
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
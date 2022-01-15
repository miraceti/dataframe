# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:58:08 2020

@author: eric
"""

from pandas import *
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

def side_by_side(*objs, **kwds):
    from pandas.core.common import adjoin
    space = kws.get('space', 4)
    reprs = [repr(obj).split('\n') for obj in objs]
    print(adjoin(space, *reprs))
    
plt.rc('figure', figsize=(10,6))

labels =['a','b','c','d','e']
s = Series(np.random.randn(5), index=labels)
s

'b' in s

s['b']

df = pd.DataFrame({'a':np.random.randn(6),'b':['foo','bar']*3,'c':np.random.randn(6)})
df

pd.set_option('display.notebook_repr_html',False)
print(df)
pd.set_option('display.notebook_repr_html',True)
print(df)

print(df['a'])

df['d']=range(6)
print(df)
print(df.loc[1])
df.loc[2,'b']

#timeit df.get_value(2,'b')
#timeit df.loc[2,'b']

df.loc[2:4,['b','c']]


print(df.loc[df['c']>0,['b','c','d']])

print(df.loc[df['c']>0])

print(df[df['c']>0])


data ={}
for col in ['foo','bar','baz']:
    for row in ['a','b','c','c']:
        data.setdefault(col,{})[row]=np.random.randn()
print(data)
print(DataFrame(data))

del data['foo']['c']
print(data)
print(DataFrame(data))

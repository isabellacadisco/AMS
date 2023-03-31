import pandas as pd
import numpy as np
ds = pd.read_csv("D:/wdi2018.csv")

#ds.summary()
#ds.info()
#ds.columns

#ds.isna()
v=[]
v = pd.DataFrame([v])
k=ds.isna().sum()
i = 0
for i in range(len(ds.columns)):
    if ((k[i] / len(ds.iloc[:,i])) * 100) > 20:
          v.loc[0,i]=i
for i in reversed(range(len(v.columns))):
    ds=ds.drop(ds.columns[v.iloc[0,i]], axis=1)

ds2 = pd.read_csv('D:/income.csv')

ds.loc[:,140]=0
for i in range(len(ds)):
    for j in range(len(ds2)):
        if ds2.iloc[j,0] == ds.iloc[i,3]:
            ds.loc[i,140]= ds2.iloc[j,2]
            
            
ds.to_csv(r'D:\incomeadded.csv', index=False)

       

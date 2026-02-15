"""
vertically - row wise
horizontally - column wise

pd.concate([df1,df2], axis=0, ignore_index=True)
ignore_index = True
"""

import pandas as pd

#region1
df_region1 = pd.DataFrame({
    'CustomerID': [1,2],
    'Name': ['Gopal','Raju']
})

#region2
df_region2 = pd.DataFrame({
    'CustomerID': [3,4],
    'Name': ['Shyam','Baburai']
})

#concatenate vertically
df_concatenate_v = pd.concat([df_region1,df_region2],ignore_index=True)
print(df_concatenate_v)

#concatenate horizontally
df_concatenate_h = pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concatenate_h)
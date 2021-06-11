import pandas as pd
import numpy as np
import copy

np.random.seed(0)
df1 = pd.DataFrame(np.random.randint(0, 15, size=(3, 5)), index=['a', 'b', 'c'], columns=['x1', 'x2', 'x3', 'x4', 'x5'])
df2 = copy.deepcopy(df1)
print(df1)

# numpy select
conds = [
    df1['x1'] == 12,
    df1['x1'] == 3,
    df1['x1'] == 2,
]
choices = df2['x3']

df1['x5'] = np.select(condlist=conds, choicelist=choices)
print(df1)

# solution 3
s3 = copy.deepcopy(df1)
s3.loc[s3['x1'] == 12, 'new_col'] = s3['x1']
s3.loc[s3['x1'] == 3, 'new_col'] = s3['x2']
s3.loc[s3['x3'] == 7, 'new_col'] = s3['x1']
print(s3)
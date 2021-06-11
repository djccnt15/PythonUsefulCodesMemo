import pandas as pd
import numpy as np
import copy

np.random.seed(0)
df = pd.DataFrame(np.random.randint(0, 15, size=(3, 5)), index=['a', 'b', 'c'], columns=['x1', 'x2', 'x3', 'x4', 'x5'])
print(df)
val = df.iloc[0][0]

# solution 1
s1 = copy.deepcopy(df)
for index, row in s1.iterrows():
    if row[0] == val:
        row[4] = val * 10
        s1.loc[index] = row
print(s1)

# solution 2
s2 = copy.deepcopy(df)
s2["new_col"] = np.where(s2["x1"]==val, 1, 100)
print(s2)
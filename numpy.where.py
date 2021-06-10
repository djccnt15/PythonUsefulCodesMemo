import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame(np.random.randint(0, 15, size=(3, 5)), index=['a', 'b', 'c'], columns=['x1', 'x2', 'x3', 'x4', 'x5'])
df['new_col'] = [3, 1, 5]
print(df)
val = df.iloc[0][0]

# solution 1
sol1 = df[:]
for index, row in sol1.iterrows():
    row = list(row)
    if row[0] == val:
        row[5] = val * 10
        sol1.loc[index] = row
print(sol1)

# solution 2
sol2 = df[:]
sol2["new_col"] = np.where(sol2["x1"]==val, 1, 100)
print(sol2)
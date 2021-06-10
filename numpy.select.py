import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame(np.random.randint(0, 15, size=(3, 5)), index=['a', 'b', 'c'], columns=['x1', 'x2', 'x3', 'x4', 'x5'])
df['new_col'] = [3, 1, 5]
print(df)

# numpy select
args = df.loc[df.index]
print(args)
conds = [
    df['x1'] == '12',
    df['x1'] == '3',
    df['x1'] == '2',
]
choices = [
    args['x1'],
    args['x2'],
    args['x3'],
]
df['test_col'] = np.select(condlist=conds, choicelist=choices)
print(df)
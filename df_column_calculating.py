import pandas as pd

a = [1, 2, 3, 4]

df = pd.DataFrame()
df['a'], df['b'] = a, a

df.loc[df['a'] <= 2, 'c'] = df['a'] - df['b']
df.loc[df['a'] > 2, 'c'] = df['a'] + df['b']

print(df)

import pandas as pd

a = {'A':[1, 2, 3], 'B':[2, 4, 6]}
d = pd.DataFrame.from_dict(a)
print(d)

d.columns = list(map(lambda x: x.lower(), list(d.columns)))
print(d)

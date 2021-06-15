import pandas as pd

a = '2013 소상공인 실태조사'
b = '2014 소상공인 실태조사'
data_list = [a, b]
df = pd.DataFrame(data_list)
print(df)

df.to_csv('./sample.csv', encoding='utf-8-sig')
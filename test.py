"""
@Author: yanzx
@Date: 2023/2/1 22:57
@Description: 
"""

import pandas as pd


# 聚合过滤 ★
df = pd.DataFrame(
    {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
     'B': [1, 2, 3, 4, 5, 6],
     'C': [2.0, 5., 8., 1., 2., 9.]})
print(df)
grouped = df.groupby('A')
print(grouped)
df_res = grouped.filter(lambda x: x['B'].mean() > 3)
print(df_res)

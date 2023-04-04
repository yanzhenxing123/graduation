"""
@Author: yanzx
@Date: 2023/2/1 22:57
@Description: 
"""

import pandas as pd
import re

# 聚合过滤 ★
# df = pd.DataFrame(
#     {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
#      'B': [1, 2, 3, 4, 5, 6],
#      'C': [2.0, 5., 8., 1., 2., 9.]})
# print(df)
# grouped = df.groupby('A')
# print(grouped)
# df_res = grouped.filter(lambda x: x['B'].mean() > 3)
# print(df_res)


def main():
    # 我一定要好好准备复试啊
    import re

    s = '\\hline$ x $ & $ -3 $ & $ -2 $ & $ -1 $ & 0 \\\\'
    matches = re.findall('&\s*([^&]+)\s*&', s)
    print(matches)


if __name__ == '__main__':
    main()



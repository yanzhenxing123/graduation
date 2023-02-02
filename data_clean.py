"""
@Author: yanzx
@Date: 2023/2/1 22:27
@Description: 数据清洗
"""

import numpy as np
import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    数据清理
    :param data:
    :return:
    """
    # 3. 重复迭代1和2
    while True:
        # 1. 删除购买物品出现次数少于k次的用户(k是一个可控的值),建议先设置成5 聚合计数条件删除
        count = len(df)
        k1 = 5
        df = df.groupby('user_id').filter(lambda x: len(x) >= k1)

        # 2. 删除被用户购买少于k次的物品，k值建议设置成5
        k2 = 5
        df = df.groupby('item_id').filter(lambda x: len(x) >= k2)
        if count == len(df):
            break

    return df

if __name__ == '__main__':
    ratings_data = pd.read_csv(filepath_or_buffer="data/ratings_data.txt",
                               header=None,
                               names=["user_id", "item_id", "rating_value"],
                               delimiter=r"\s+")
    # trust_data = pd.read_table("data/trust_data.txt")
    ratings_data = clean(ratings_data)

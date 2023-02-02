"""
@Author: yanzx
@Date: 2023/2/1 22:27
@Description: 数据清洗
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Set


def clean(df: pd.DataFrame):
    """
    数据清理
    :param data:
    :return: train, test, validate
    """
    # 3. 重复迭代1和2 最后剩余20397条数据
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
    print("----------------------------------------------finish task1, 2, 3-------------------------------------------")
    print(f"经过1,2,3处理后，剩余数据{len(df)}条, len(user_ids)={len(df['user_id'].unique())}")

    # 4. 对每一个用户，先分出20%的数据存入测试集，剩下的数据10%存入验证集，剩下的为训练集
    user_ids = df['user_id'].unique()
    train = pd.DataFrame(columns=["user_id", "item_id", "rating_value"])
    validate = pd.DataFrame(columns=["user_id", "item_id", "rating_value"])
    test = pd.DataFrame(columns=["user_id", "item_id", "rating_value"])
    for user_id in user_ids:
        one_user_df = df[df['user_id'] == user_id]
        # 先分出20%的数据存入测试集
        data_train, data_test = train_test_split(one_user_df, test_size=0.2, random_state=1234)
        # 剩下的数据10%存入验证集
        data_train, data_validate = train_test_split(data_train, test_size=0.1, random_state=1234)
        train = train.append(data_train)
        test = test.append(data_test)
        validate = validate.append(data_validate)
    print("-----------------------------------------------finish task4------------------------------------------------")
    print(f"经过4处理后, train: {len(train)}条, test: {len(test)}条, validate: {len(validate)}条, 剩余数据{len(train) + len(test) + len(validate)}条")

    # 5. 检查测试集和验证集里的每条记录，如果某条记录的用户id和物品id没有在训练集中出现过，则删掉这条记录。
    train, test, validate = check_data(train, test, validate)
    print("-----------------------------------------------finish task5------------------------------------------------")
    print(f"经过5处理后, train: {len(train)}条, test: {len(test)}条， validate: {len(validate)}条, 剩余数据{len(train) + len(test) + len(validate)}条")

    return train, test, validate


def check_data(train: pd.DataFrame, test: pd.DataFrame, validate: pd.DataFrame):
    """
    如果某条记录的用户id和物品id没有在训练集中出现过，则删掉这条记录。
    :param df: test or validate
    :return:
    """
    train_user_ids = set(train['user_id'].unique())
    train_item_ids = set(train['item_id'].unique())

    # unhashable DataFrame不可被hash 不能这样用
    # test.groupby('user_id').filter(lambda x: x in list(train_user_ids))
    # df = df.groupby('user_id').filter(lambda x: len(x) >= k1)
    def check(df: pd.DataFrame):
        for user_id in df['user_id'].unique():
            if user_id not in train_user_ids:
                df = df[df['user_id'] != user_id]

        for item_id in df['item_id'].unique():
            if item_id not in train_item_ids:
                df = df[df['item_id'] != item_id]
        return df

    return train, check(test), check(validate)


if __name__ == '__main__':
    ratings_data = pd.read_csv(filepath_or_buffer="data/ratings_data.txt",
                               header=None,
                               names=["user_id", "item_id", "rating_value"],
                               delimiter=r"\s+")
    # trust_data = pd.read_csv("data/trust_data.txt")

    # 使用20%的数据的进行测试
    _, ratings_data = train_test_split(ratings_data, test_size=0.2, random_state=1234)
    train, test, validate = clean(ratings_data)

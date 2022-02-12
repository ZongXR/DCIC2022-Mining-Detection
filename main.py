# -*- coding: utf-8 -*-
import pandas as pd


if __name__ == '__main__':
    cons_info = pd.read_csv("./data/训练组_比特币挖矿_档案明细（20211220）.csv", index_col=0, quotechar='"', encoding="gbk")
    elec_day = pd.read_csv("./data/训练组_比特币挖矿_日用电明细（20211217）.csv")
    elec_month = pd.read_csv("./data/训练组_比特币挖矿_月用电明细（20211217）.csv")
    target = pd.read_csv("./data/训练组_比特币挖矿_疑似用户明细（20211217）.csv ", index_col="id")
    print(target.head())



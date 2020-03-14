#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#

'''
    根据你的 贷款总额，分期数 和 还款期数，计算年化利率
'''

# 请填写以下三个值

# 1. 您的贷款总额
Total_money = 20000

# 2. 您的总分期数
Total_month = 12

# 3. 您的每期还款额
Per_month_money = 2266.67

# 4. 一次性手续费，单位 %
Once_rate = 0

'''
    以下为代码部分，请勿动，只需要填写上面三个数值即可
'''

import numpy as np

def r(real_money, n = 2):
    return round(real_money, n)

def cal_annual_rate(total_money, total_month, per_month_money, once_rate):
    #
    # total_money      总计借款数量
    # per_month_money  每期还款额度
    # total_month      总共分期期数

    total_money -= (total_money * once_rate / 100)
    load_infos = [-total_money]
    for month_index in range(total_month):
        load_infos.append(per_month_money)

    # 计算内部收益率
    per_month_rate = np.irr(load_infos)

    # 计算年化收益率（复利公式）
    year_rate = (per_month_rate + 1) ** 12 - 1

    #月均还款(本金+利息)
    t_per_month_money = total_money * per_month_rate * pow((1 + per_month_rate), total_month)/(pow((1 + per_month_rate), total_month) - 1)

    #还款利息总和
    t_total_rate_money = total_month * total_money * per_month_rate * pow((1 + per_month_rate), total_month)/(pow(1 + per_month_rate, total_month) - 1) - total_money


    print("\n\n{:^70}\n\n\n贷款总额为 {}, 总分 {} 期, 每期还款 {} 元，利息如下：\n".format("信用卡分期利息计算", total_money, total_month, per_month_money))
    print("实际月利息 = {}%, 名义年利率 = {}%，实际年利率 = {}%\n".format(r(per_month_rate * 100), r(12 * per_month_rate * 100), r(year_rate * 100)))
    print("每月月供为 = {:.2f}, 总利息 = {:.2f}\n".format(r(t_per_month_money), r(t_total_rate_money)))


    # 第一个月还款利息
    first_interest = total_money * per_month_rate
    # 剩余利息
    remain_rate_money = t_total_rate_money - first_interest
    # 剩余本金
    remain_money = total_money - (t_per_month_money - first_interest)

    print("----- 等额本息计算, 以 %s 个月为例 -----\n" % total_month)
    print("第 {:-2d} 个月应还利息为 {:8.02f}, 应还本金为 {:8.02f}, 还款总额为 {:8.02f}，剩余欠款 {:8.02f} ".format (1, first_interest, r(t_per_month_money - first_interest), t_per_month_money, r(remain_money)))
    # 第 2 - n 个月还款利息
    for cur_month in range(2, total_month + 1):
        cur_interest = (total_money * per_month_rate - t_per_month_money)*pow((1 + per_month_rate), (cur_month - 1)) + t_per_month_money
        cur_base = t_per_month_money - cur_interest
        remain_money = remain_money - cur_base
        print("第 {:-2d} 个月应还利息为 {:8.02f}, 应还本金为 {:8.02f}, 还款总额为 {:8.02f}，剩余欠款 {:8.02f} ".format(cur_month, r(cur_interest), r(cur_base), t_per_month_money, abs(r(remain_money))))

    print("\n\n====== 假如 等额本金还款，以 %s 个月为例 ======" % total_month)
    #每月应还本金
    per_base_money = total_money / total_month
    t_total_rate_money_2 = 0
    remain_money = total_money
    for cur_month in range(1, total_month + 1):
        cur_interest = (total_money - per_base_money *(cur_month - 1)) * per_month_rate #每月应还利息
        t_total_rate_money_2 += cur_interest
        cur_total_money = per_base_money + cur_interest
        remain_money = remain_money - per_base_money
        print("第 {:-2d} 个月应还利息为 {:8.02f}, 应还本金为 {:8.02f}, 还款总额为 {:8.02f}，剩余欠款 {:8.02f}".format(cur_month, r(cur_interest), r(per_base_money), r(cur_total_money), abs(r(remain_money))))

    print("\n等额本金还款，总利息 = {:.2f}, 比等额本息少 {:.2f}\n".format(r(t_total_rate_money_2), r(t_total_rate_money - t_total_rate_money_2)))

if __name__ == "__main__":
    cal_annual_rate(Total_money,  Total_month, Per_month_money, Once_rate)


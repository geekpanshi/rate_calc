#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# Github：https://github.com/geekpanshi/rate_calc

'''
    根据你的 贷款总额、分期数 等信息，计算年化利率
'''

# 请填写以下三个值

# 1. 您的贷款总额
Total_money = 100000

# 2. 您的总分期数
Total_month = 12

##### 请设置你要还款的方式
'''
    Type = 1 ：已知 每期还款现金 和 一次性手续费百分比
    Type = 2 ：已知 月利息       和 每月服务费
    Type = 3 ：已知 月利息       和 总服务费
    Type = 4 : 已知 日息         和 每月等额还款
    Type = 5 ：已知 日息         和 先息后本还款
'''
Type = 1

#### 1. Type = 1：已知 每期还款现金 和 一次性手续费百分比
# 1.1 您的每期还款额
Per_month_money_1 = 2266.67
# 1.2 一次性手续费，单位 %
Once_rate_1 = 0

#### 2. Type = 2 ：已知 月利息 和 每月服务费
# 2.1 每月的利息，单位 %，
Per_month_rate_2 = 0.5
# 2.2 每月的服务费，单位 %
Per_month_other_2 = 0.1

#### 3. Type = 3 ：已知 月利息 和 总服务费
# 3. 每月的利息，单位 %，
Per_month_rate_3 = 0.5

# 4. 服务费总额
Per_month_other_3 = 20000

#### 4. Type = 4 ：已知 日息 和 每月等额，万 3.5 的利息
Per_day_rate_1 = 3.5

#### 5. Type = 4 ：已知 日息 和 先息后本，万 3.5 的利息
Per_day_rate_2 = 3.5

'''
    以下为代码部分，请勿动，只需要填写上面三个数值即可
'''

import numpy as np

def r(real_money, n = 2):
    return round(real_money, n)

def cal_annual_rate_2(total_money, total_month, per_month_rate, per_month_other = 0.0):
    per_month_money = total_money / 12.0   + total_money * (per_month_rate + per_month_other) / 100.0
    cal_annual_rate(total_money, total_month, per_month_money)

def cal_annual_rate_3(total_money, total_month, per_month_rate, per_month_other = 0.0):
    real_money = total_money - per_month_other
    per_month_money = total_money / 12.0 + total_money * per_month_rate / 100.000
    cal_annual_rate(real_money, total_month, per_month_money)

def cal_annual_rate_4(total_money, total_month, per_day_rate_1, per_month_other = 0.0):
    cal_annual_rate(total_money, total_month, 0, per_month_other, per_day_rate_1)

def cal_annual_rate_5(total_money, total_month, per_day_rate):
    # total_money      总计借款数量
    # total_month      总共分期期数
    load_infos = [-total_money]
    month_rates = (per_day_rate / 10000.0 * total_money) * 365.0 / 12.0
    for month_index in range(total_month - 1):
        load_infos.append(month_rates)
    load_infos.append(month_rates + total_money)
    per_month_rate = np.irr(load_infos)

    # 计算年化收益率（复利公式）
    year_rate = (per_month_rate + 1) ** 12 - 1

    #还款利息总和
    t_total_rate_money = (per_day_rate / 10000.0 * total_money) * 365.0

    print("\n\n{:^70}\n\n\n贷款总额：{}, 总分 {} 期, 日息 万分之{}，还款方式：先息后本:\n".format("信用卡分期利息计算", total_money, total_month, per_day_rate))
    print("利息如下：实际月利息 = {}%, 名义年利率 = {}%，实际年利率 = {}%\n".format(r(per_month_rate * 100), r(12 * per_month_rate * 100), r(year_rate * 100)))
    print("还款细节：每 1 - {} 月月供为 {:.2f}, 第 {} 个月月供为 {}， 总利息 {:.2f}\n".format(total_month - 1, r(month_rates), total_month,  r(total_money +  month_rates), r(month_rates) * 12.0))

def cal_annual_rate(total_money, total_month, per_month_money, once_rate = 0, per_day_rate = 0):
    #
    # total_money      总计借款数量
    # per_month_money  每期还款额度
    # total_month      总共分期期数
    if not per_day_rate:
        total_money -= (total_money * once_rate / 100)
        load_infos = [-total_money]
        for month_index in range(total_month):
            load_infos.append(per_month_money)

        # 计算内部收益率
        per_month_rate = np.irr(load_infos)
    else:
        per_month_rate = per_day_rate * 365.0 / 12.0 / 10000.0

    # 计算年化收益率（复利公式）
    year_rate = (per_month_rate + 1) ** 12 - 1

    #月均还款(本金+利息)
    t_per_month_money = total_money * per_month_rate * pow((1 + per_month_rate), total_month)/(pow((1 + per_month_rate), total_month) - 1)

    #还款利息总和
    t_total_rate_money = total_month * total_money * per_month_rate * pow((1 + per_month_rate), total_month)/(pow(1 + per_month_rate, total_month) - 1) - total_money


    print("\n\n{:^70}\n\n\n贷款总额为 {}, 总分 {} 期, 每期还款 {} 元，利息如下：\n".format("信用卡分期利息计算", total_money, total_month, r(t_per_month_money)))
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
    if Type == 2:
        cal_annual_rate_2(Total_money, Total_month, Per_month_rate_2, Per_month_other_2)
    elif Type == 3:
        cal_annual_rate_3(Total_money, Total_month, Per_month_rate_3, Per_month_other_3)
    elif Type == 4:
        cal_annual_rate_4(Total_money, Total_month, Per_day_rate_1, 0)
    elif Type == 5:
        cal_annual_rate_5(Total_money, Total_month, Per_day_rate_2)
    else:
        cal_annual_rate(Total_money,  Total_month, Per_month_money_1, Once_rate_1)

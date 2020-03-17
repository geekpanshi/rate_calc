#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# Github：https://github.com/geekpanshi/rate_calc

'''
    根据你的 存款额度、年利息、存款期限，计算利息

    复利计算器是在上一年度利息的收益加到下一年的本金来计算的。
'''

# 请填写以下一些值

#### 计算类型
'''
    Type = 1 ：已知 存款额、存款期限 和 年化，算利息。
    Type = 2 ：已知 初期存款、定存周期、定存额度 和 存款期限，算利息
    Type = 3 ：已知 初期存款、定存周期、定存额度 和 最终总和，算年化利率
    Type = 4 ：已知 年化利率、定存周期、定存额度 和 最终总和，算最初需要的投入资金
    Type = 5 ：已知 贷款利息、贷款周期、贷款额，算等额本息/等额本金月供

'''
Type = 1

#### 1. Type = 1 ：已知 存款额、存款期限 和 年化，算利息
# 1.1 您的贷款总额
T_1_total_money = 1000
# 1.2 您的存款年限
'''
    一个月等于多少年:
    1  个月 = 0.08 年
    2  个月 = 0.17 年
    3  个月 = 0.25 年
    4  个月 = 0.33 年
    5  个月 = 0.42 年
    6  个月 = 0.50 年
    7  个月 = 0.58 年
    8  个月 = 0.67 年
    9  个月 = 0.75 年
    10 个月 = 0.83 年
    11 个月 = 0.92 年
'''
T_1_total_years = 5
# 1.3 银行承诺的年年化利息，单位 %
T_1_year_rate = 3


#### 2. Type = 2 ：已知 初期存款、定存周期、定存额度 和 存款期限，算利息
# 2.1 首次存款金额
T_2_first_money = 1000
# 2.2 存款期限，单位年
T_2_total_years = 5
# 2.3 定存额度
T_2_per_save = 0
# 2.4 存款间隔，月份
T_2_time_interval = 12
# 2.5 年化利率
T_2_year_rate = 3


#### 3. Type = 3 ：已知 初期存款、定存周期、定存额度 和 最终总和，算年化利率
# 3.1 年化利率
T_3_first_money = 1000
# 3.2 存款期限，单位年
T_3_total_years = 5
# 3.3 定存额度
T_3_per_save = 10
# 3.4 存款间隔，月份
T_3_time_interval = 3
# 3.5 最终本息总和
T_3_last_total_money = 1376.10


#### 4. Type = 4 ：已知 年化利率、定存周期、定存额度 和 最终总和，算最初需要的投入资金
# 4.1 首次存款金额
T_4_year_rate = 3
# 4.2 存款期限，单位年
T_4_total_years = 5
# 4.3 定存额度
T_4_per_save = 10
# 4.4 存款间隔，月份
T_4_time_interval = 3
# 4.5 最终本息总和
T_4_last_total_money = 1376.10


#### 5. Type = 5 ：已知 贷款利息、贷款周期、贷款额，算月供
# 5.1 年化利率
T_5_year_rate = 4.66
# 5.2 存款期限，单位年
T_5_total_years = 20
# 5.3 贷款总额
T_5_total_money = 434000

import numpy as np

def r(real_money, n = 2):
    return round(real_money, n)

### 年利率是 3%，存款为 1000，然后每个季度都会存 10 元，那么五年后能拿到多少钱呢？
def cal_annual_rate_2(first_money, total_years, per_save, time_interval, year_rate):
    '''
    def fv(rate, nper, pmt, pv, when='end'):
        ...
        参数 —— 计算未来的价值
        rate ：存款/贷款每期的利率
        nper ：存款/贷款期数
        pmt  ：存款/贷款每期支付的金额
        pv   ：当前的存款/贷款金额
    '''
    result = np.fv(year_rate * time_interval / 12 / 100, total_years * 12 / time_interval, -per_save, -first_money)

    print("\n\n{:^70}\n\n".format("定投利息计算器"))

    print("年利率是 {}%，初期存款为 {}，然后每 {} 个月都会存 {} ，那么 {} 年后能拿到 {} ".format(year_rate, first_money, time_interval, per_save, total_years, r(result)))


def cal_annual_rate_3(first_money, total_years, per_save, time_interval, last_total_money):
    '''
    def rate(nper, pmt, pv, fv, when='end', guess=None, tol=None, maxiter=100):
        ...
        参数 —— 计算利率
        nper ：期数
        pmt  ：每期的存款/贷款金额
        pv   ：当前的存款/贷款金额
        fv   ：future value
    '''
    result = np.rate(total_years * 12 / time_interval, -per_save, -first_money, last_total_money)


    print("\n\n{:^70}\n\n".format("定投利率计算器"))
    print("初期存款为 {}，然后每 {} 个月都会存 {} ，那么 {} 年后能拿到 {}，则年化利率为 {}%。".format(first_money, time_interval, per_save, total_years, last_total_money, r(result  * 12 / time_interval * 100)))


def cal_annual_rate_4(year_rate, total_years, per_save, time_interval, last_total_money):
    '''
    def pv(rate, nper, pmt, fv=0, when='end'):
        ...
        参数 —— 根据未来计算现在的价值
        rate ：存款/贷款每期的利率
        nper ：存款/贷款期数
        pmt  ：存款/贷款每期支付的金额
        fv   ：未来的存款/贷款金额
    '''
    result = np.pv(year_rate * time_interval / 12 / 100, total_years *  12 / time_interval, -per_save, last_total_money)

    print("\n\n{:^70}\n\n".format("定投首次存款计算器"))
    print("年利率是 {}%，然后每 {} 个月都会存 {} ，那么 {} 年后能拿到 {}，则初期需要投入 {} ".format(year_rate, time_interval, per_save, total_years, last_total_money, r(-result)))


def cal_annual_rate_5(year_rate, total_years, total_money):
    '''
    def pmt(rate, nper, pv, fv=0, when='end'):
        ...
        参数 —— 根据本金和利率计算出每期需要支付的金额
        rate ：存款/贷款每期的利率
        nper ：存款/贷款期数
        pv   ：存款/贷款金额
    '''

    total_month = total_years * 12


    result = np.pmt(year_rate / 12 / 100, total_month, total_money)

    load_infos = [-total_money]
    for month_index in range(total_month):
        load_infos.append(-result)



    per_month_rate = np.irr(load_infos)

    t_total_rate_money = total_month * total_money * per_month_rate * pow((1 + per_month_rate), total_month)/(pow(1 + per_month_rate, total_month) - 1) - total_money


    per_base_money = total_money / total_month

    first_total = per_base_money + total_money * per_month_rate
    last_total  = per_base_money + (total_money - per_base_money * total_month) * per_month_rate

    t_total_rate_money_2 = 0
    for cur_month in range(1, total_month + 1):
        cur_interest = (total_money - per_base_money *(cur_month - 1)) * per_month_rate #每月应还利息
        t_total_rate_money_2 += cur_interest


    print("\n\n{:^70}\n\n\n贷款总额为 {}, 总分 {} 期, 年化利息 {}%，利息及月供如下：\n".format("分期月供计算器", total_money, total_month, r(year_rate)))
    print("等额本息：利息总和 {}，月供 {}".format(r(t_total_rate_money), r(-result)))
    print("\n等额本金：利息总和 {}，首月 {}，最后一个月 {}，".format(r(t_total_rate_money_2), r(first_total), r(last_total)))
    print("\n等额本金 比 等额本息 总计少付利息：{}".format(r(r(t_total_rate_money) - r(t_total_rate_money_2))))


def cal_annual_rate_1(total_money,  total_years, year_rate):
    #
    # total_money   存款额度
    # total_years   存款年限
    # year_rate     年化利率
    total_rate_m = total_money * (1 + year_rate / 12 / 100.00) ** (total_years * 12)


    total_rate_y = total_money * (1 + year_rate/ 100.00) ** total_years

    print("\n\n{:^40}\n\n\n存款总额为 {}, 存款期限为 {} 年, 年化利率为 {}%\n".format("存款利息计算器", total_money, total_years, r(year_rate)))
    print("以 年 复利，最终本息合计 = {}, 其中利息 = {}，\n".format(r(total_rate_y), r(total_rate_y - total_money)))
    print("以 月 复利，最终本息合计 = {}, 其中利息 = {}。".format(r(total_rate_m), r(total_rate_m - total_money)))

if __name__ == "__main__":
    if Type  == 2:
        cal_annual_rate_2(T_2_first_money, T_2_total_years, T_2_per_save, T_2_time_interval, T_2_year_rate)
    elif Type == 3:
        cal_annual_rate_3(T_3_first_money, T_3_total_years, T_3_per_save, T_3_time_interval, T_3_last_total_money)
    elif Type == 4:
        cal_annual_rate_4(T_4_year_rate, T_4_total_years, T_4_per_save, T_4_time_interval, T_4_last_total_money)
    elif Type == 5:
        cal_annual_rate_5(T_5_year_rate, T_5_total_years, T_5_total_money)
    else:
        cal_annual_rate_1(T_1_total_money, T_1_total_years, T_1_year_rate)

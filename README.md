## 分期真实利率计算器

<!--ts-->
   * [分期真实利率计算器](#分期真实利率计算器)
      * [1. 例子说明](#1-例子说明)
         * [1.1 Excel 12 期分期利息计算法：](#11-excel-12-期分期利息计算法)
         * [1.2 Python 分期利息计算法（不限分期数目）：](#12-python-分期利息计算法不限分期数目)
      * [2. 计算几种情况下的实际利率和还款细节举例](#2-计算几种情况下的实际利率和还款细节举例)
         * [2.1 Type = 1：<a href="https://onlinegdb.com/S1m6AZAr8" rel="nofollow">已知 每期还款现金 和 一次性手续费百分比</a>](#21-type--1已知-每期还款现金-和-一次性手续费百分比)
         * [2.2 Type = 2 ：<a href="https://onlinegdb.com/Bk5C0ZRrI" rel="nofollow">已知 月利息 和 每月服务费</a>](#22-type--2-已知-月利息-和-每月服务费)
         * [2.3 Type = 3 ：<a href="https://onlinegdb.com/HJBV1MRHI" rel="nofollow">已知 月利息 和 总服务费</a>](#23-type--3-已知-月利息-和-总服务费)
         * [2.4 Type = 4 ：<a href="https://onlinegdb.com/rJg8U1MArU" rel="nofollow">已知 日息 和 每月等额，万 3.5 的利息</a>](#24-type--4-已知-日息-和-每月等额万-35-的利息)
         * [2.5 Type = 5 ：<a href="https://onlinegdb.com/H1pw1GAB8" rel="nofollow">已知 日息 和 先息后本，万 3.5 的利息</a>](#25-type--5-已知-日息-和-先息后本万-35-的利息)
         * [2.6 Type = 6 ：<a href="https://onlinegdb.com/rkzp1MRrU" rel="nofollow">已知 每期还款额都不相等，求实际的利息</a>](#26-type--6-已知-每期还款额都不相等求实际的利息)
      * [3. 计算几种情况下的存款利息和利率情况](#3-计算几种情况下的存款利息和利率情况)
         * [3.1 Type = 1 ：<a href="https://onlinegdb.com/B1fHQMRrU" rel="nofollow">已知 存款额、存款期限 和 年化，算利息</a>](#31-type--1-已知-存款额存款期限-和-年化算利息)
         * [3.2 Type = 2 ：<a href="https://onlinegdb.com/SyWImMASU" rel="nofollow">已知 初期存款、定存周期、定存额度 和 存款期限，算利息</a>](#32-type--2-已知-初期存款定存周期定存额度-和-存款期限算利息)
         * [3.3 Type = 3 ：<a href="https://onlinegdb.com/HyGvmG0SU" rel="nofollow">已知 初期存款、定存周期、定存额度 和 最终总和，算年化利率</a>](#33-type--3-已知-初期存款定存周期定存额度-和-最终总和算年化利率)
         * [3.4 Type = 4 ：<a href="https://onlinegdb.com/BkRD7zRrU" rel="nofollow">已知 年化利率、定存周期、定存额度 和 最终总和，算最初需要的投入资金</a>](#34-type--4-已知-年化利率定存周期定存额度-和-最终总和算最初需要的投入资金)
         * [3.5 Type = 5 ：<a href="https://onlinegdb.com/Hk9rQMXU8" rel="nofollow">已知 贷款利息、贷款周期、贷款额，算等额本息/等额本金月供</a>](#35-type--5-已知-贷款利息贷款周期贷款额算等额本息等额本金月供)
<!--te-->

> 很多同学不会算银行的分期真实利率的，这里提供两个方式去帮助你计算银行分期情况下的真实利率。
>
> 银行公布的利率转换公式：`年利率 = 月利息 * 12 = 日利息 * 360`

### 1. 例子说明
> 以借 20000 元，分 12 期，每个月还款 2266.67 元 ，问年化利率是多少？

#### 1.1 Excel 12 期分期利息计算法：

1. 计算文件
>
> [银行 12 期分期利息计算表](/银行-12-期分期利息计算表.xlsx)

2. 例子
>
> [2 万元分 12 期，月还 2266.67，计算链接](/银行-12-期分期利息计算表.xlsx)

3. 计算结果
>
> ![银行 12 期分期利息计算表](/pics/rate_calc_1.png)

#### 1.2 Python 分期利息计算法（不限分期数目）：

1. 计算源码
>
> [Python 分期利息计算法](/interst_rate_calc.py)

2. 例子
>
> [2 万元分 12 期，月还 2266.67，计算链接](https://onlinegdb.com/BkvybphrU)

3. 计算结果
>
> ![银行 12 期分期利息计算结果](/pics/rate_calc_2.png)

### 2. 计算几种情况下的实际利率和还款细节举例
> 可以根据你的 贷款总额、分期数 等信息，计算年化利率
>
>> 1. 您的贷款总额：`Total_money = 20000`
>> 2. 您的总分期数：`Total_month = 12`
>
> 可以根据 类型参数 Type 选择不同的情况计算利息

#### 2.1 Type = 1：[已知 每期还款现金 和 一次性手续费百分比](https://onlinegdb.com/S1m6AZAr8)
> 1.1 您的每期还款额：`T_1_per_month_money = 2266.67`
>
> 1.2 一次性手续费，单位 %：`T_1_once_rate = 0`

#### 2.2 Type = 2 ：[已知 月利息 和 每月服务费](https://onlinegdb.com/Bk5C0ZRrI)
> 2.1 每月的利息，单位 %：`T_2_per_month_rate = 0.5`
>
> 2.2 每月的服务费，单位 %：`T_2_per_month_other = 0.1`

#### 2.3 Type = 3 ：[已知 月利息 和 总服务费](https://onlinegdb.com/HJBV1MRHI)
> 3.1 每月的利息，单位 %： `T_3_per_month_rate = 0.5`
>
> 3.2 服务费总额：`T_3_per_month_other = 2000`

#### 2.4 Type = 4 ：[已知 日息 和 每月等额，万 3.5 的利息](https://onlinegdb.com/rJg8U1MArU)
> 4.1 每日利息，万分之 3.5：`T_4_per_day_rate = 3.5`

#### 2.5 Type = 5 ：[已知 日息 和 先息后本，万 3.5 的利息](https://onlinegdb.com/H1pw1GAB8)
> 5.1 每日利息，万分之 3.5：`T_5_per_day_rate = 3.5`

#### 2.6 Type = 6 ：[已知 每期还款额都不相等，求实际的利息](https://onlinegdb.com/rkzp1MRrU)
> 6.1 每期还款的按顺序的列表
```python
T_6_all_month_pays = [
    167.20,
    184.00,
    186.80,
    205.00,
    108.50,
    108.50,
    105.00,
    108.50,
    105.00,
    108.50,
    108.50,
    20098.00,
]
```

### 3. 计算几种情况下的存款利息和利率情况

#### 3.1 Type = 1 ：[已知 存款额、存款期限 和 年化，算利息](https://onlinegdb.com/B1fHQMRrU)
> 1.1 您的贷款总额：`T_1_total_money = 1000`
> 1.2 您的存款年限: `T_1_total_years = 5`
```python
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
```
> 1.3 银行承诺的年年化利息，单位 %：`T_1_year_rate = 3`

#### 3.2 Type = 2 ：[已知 初期存款、定存周期、定存额度 和 存款期限，算利息](https://onlinegdb.com/SyWImMASU)
> 2.1 首次存款金额：`T_2_first_money = 1000`
>
> 2.2 存款期限，单位年：`T_2_total_years = 5`
>
> 2.3 定存额度：`T_2_per_save = 0`
>
> 2.4 存款间隔，月份：`T_2_time_interval = 12`
>
> 2.5 年化利率：`T_2_year_rate = 3`

#### 3.3 Type = 3 ：[已知 初期存款、定存周期、定存额度 和 最终总和，算年化利率](https://onlinegdb.com/HyGvmG0SU)
> 3.1 年化利率：`T_3_first_money = 1000`
>
> 3.2 存款期限，单位年：`T_3_total_years = 5`
>
> 3.3 定存额度：`T_3_per_save = 10`
>
> 3.4 存款间隔，月份：`T_3_time_interval = 3`
>
> 3.5 最终本息总和：`T_3_last_total_money = 1376.10`

#### 3.4 Type = 4 ：[已知 年化利率、定存周期、定存额度 和 最终总和，算最初需要的投入资金](https://onlinegdb.com/BkRD7zRrU)
> 4.1 首次存款金额：`T_4_year_rate = 3`
>
> 4.2 存款期限，单位年：`T_4_total_years = 5`
>
> 4.3 定存额度：`T_4_per_save = 10`
>
> 4.4 存款间隔，月份：`T_4_time_interval = 3`
>
> 4.5 最终本息总和：`T_4_last_total_money = 1376.10`

#### 3.5 Type = 5 ：[已知 贷款利息、贷款周期、贷款额，算等额本息/等额本金月供](https://onlinegdb.com/Hk9rQMXU8)
> 5.1 年化利率：`T_5_year_rate = 4.66`
>
> 5.2 存款期限，单位年：`T_5_total_years = 20`
>
> 5.3 贷款总额：`T_5_total_money = 434000`

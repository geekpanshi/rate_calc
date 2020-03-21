## 分期真实利率计算器
----

> 很多同学不会算银行的分期真实利率的，这里提供两个方式去帮助你计算银行分期情况下的真实利率。
>
> 银行公布的利率转换公式：`年利率 = 月利息 * 12 = 日利息 * 360`


### 计算几种情况下的实际利率和还款细节举例

#### [Type = 1](https://github.com/geekpanshi/rate_calc#1-type--1%E5%B7%B2%E7%9F%A5-%E6%AF%8F%E6%9C%9F%E8%BF%98%E6%AC%BE%E7%8E%B0%E9%87%91-%E5%92%8C-%E4%B8%80%E6%AC%A1%E6%80%A7%E6%89%8B%E7%BB%AD%E8%B4%B9%E7%99%BE%E5%88%86%E6%AF%94) ：已知 每期还款现金 和 一次性手续费百分比
#### [Type = 2](https://github.com/geekpanshi/rate_calc#2-type--2-%E5%B7%B2%E7%9F%A5-%E6%9C%88%E5%88%A9%E6%81%AF-%E5%92%8C-%E6%AF%8F%E6%9C%88%E6%9C%8D%E5%8A%A1%E8%B4%B9) ：已知 月利息       和 每月服务费
#### [Type = 3](https://github.com/geekpanshi/rate_calc#3-type--3-%E5%B7%B2%E7%9F%A5-%E6%9C%88%E5%88%A9%E6%81%AF-%E5%92%8C-%E6%80%BB%E6%9C%8D%E5%8A%A1%E8%B4%B9) ：已知 月利息       和 总服务费
#### [Type = 4](https://github.com/geekpanshi/rate_calc#4-type--4-%E5%B7%B2%E7%9F%A5-%E6%97%A5%E6%81%AF-%E5%92%8C-%E6%AF%8F%E6%9C%88%E7%AD%89%E9%A2%9D%E4%B8%87-35-%E7%9A%84%E5%88%A9%E6%81%AF) ：已知 日息         和 每月等额还款
#### [Type = 5](https://github.com/geekpanshi/rate_calc#5-type--5-%E5%B7%B2%E7%9F%A5-%E6%97%A5%E6%81%AF-%E5%92%8C-%E5%85%88%E6%81%AF%E5%90%8E%E6%9C%AC%E4%B8%87-35-%E7%9A%84%E5%88%A9%E6%81%AF) ：已知 日息         和 先息后本还款
#### [Type = 6](https://github.com/geekpanshi/rate_calc#6-type--6-%E5%B7%B2%E7%9F%A5-%E6%AF%8F%E6%9C%9F%E8%BF%98%E6%AC%BE%E9%A2%9D%E9%83%BD%E4%B8%8D%E7%9B%B8%E7%AD%89%E6%B1%82%E5%AE%9E%E9%99%85%E7%9A%84%E5%88%A9%E6%81%AF) ：已知 每期还款额都不相等，求实际的利息


### 计算几种情况下的存款利息和利率情况

#### [Type = 1](https://github.com/geekpanshi/rate_calc#1-type--1-%E5%B7%B2%E7%9F%A5-%E5%AD%98%E6%AC%BE%E9%A2%9D%E5%AD%98%E6%AC%BE%E6%9C%9F%E9%99%90-%E5%92%8C-%E5%B9%B4%E5%8C%96%E7%AE%97%E5%88%A9%E6%81%AF) ：已知 存款额、存款期限 和 年化，算利息。
#### [Type = 2](https://github.com/geekpanshi/rate_calc#2-type--2-%E5%B7%B2%E7%9F%A5-%E5%88%9D%E6%9C%9F%E5%AD%98%E6%AC%BE%E5%AE%9A%E5%AD%98%E5%91%A8%E6%9C%9F%E5%AE%9A%E5%AD%98%E9%A2%9D%E5%BA%A6-%E5%92%8C-%E5%AD%98%E6%AC%BE%E6%9C%9F%E9%99%90%E7%AE%97%E5%88%A9%E6%81%AF) ：已知 初期存款、定存周期、定存额度 和 存款期限，算利息
#### [Type = 3](https://github.com/geekpanshi/rate_calc#3-type--3-%E5%B7%B2%E7%9F%A5-%E5%88%9D%E6%9C%9F%E5%AD%98%E6%AC%BE%E5%AE%9A%E5%AD%98%E5%91%A8%E6%9C%9F%E5%AE%9A%E5%AD%98%E9%A2%9D%E5%BA%A6-%E5%92%8C-%E6%9C%80%E7%BB%88%E6%80%BB%E5%92%8C%E7%AE%97%E5%B9%B4%E5%8C%96%E5%88%A9%E7%8E%87) ：已知 初期存款、定存周期、定存额度 和 最终总和，算年化利率
#### [Type = 4](https://github.com/geekpanshi/rate_calc#4-type--4-%E5%B7%B2%E7%9F%A5-%E5%B9%B4%E5%8C%96%E5%88%A9%E7%8E%87%E5%AE%9A%E5%AD%98%E5%91%A8%E6%9C%9F%E5%AE%9A%E5%AD%98%E9%A2%9D%E5%BA%A6-%E5%92%8C-%E6%9C%80%E7%BB%88%E6%80%BB%E5%92%8C%E7%AE%97%E6%9C%80%E5%88%9D%E9%9C%80%E8%A6%81%E7%9A%84%E6%8A%95%E5%85%A5%E8%B5%84%E9%87%91) ：已知 年化利率、定存周期、定存额度 和 最终总和，算最初需要的投入资金
#### [Type = 5](https://github.com/geekpanshi/rate_calc#5-type--5-%E5%B7%B2%E7%9F%A5-%E8%B4%B7%E6%AC%BE%E5%88%A9%E6%81%AF%E8%B4%B7%E6%AC%BE%E5%91%A8%E6%9C%9F%E8%B4%B7%E6%AC%BE%E9%A2%9D%E7%AE%97%E7%AD%89%E9%A2%9D%E6%9C%AC%E6%81%AF%E7%AD%89%E9%A2%9D%E6%9C%AC%E9%87%91%E6%9C%88%E4%BE%9B) ：已知 贷款利息、贷款周期、贷款额，算等额本息/等额本金月供

### 例子说明
> 以借 20000 元，分 12 期，每个月还款 2266.67 元 ，问年化利率是多少？

#### 方法一，Excel 12 期分期利息计算法：

##### 计算文件
>
> [银行 12 期分期利息计算表](/银行-12-期分期利息计算表.xlsx)

##### 例子
>
> [2 万元分 12 期，月还 2266.67，计算链接](/银行-12-期分期利息计算表.xlsx)

##### 计算结果
>
> ![银行 12 期分期利息计算表](/pics/rate_calc_1.png)

#### 方法二，Python 分期利息计算法（不限分期数目）：

##### 计算源码
>
> [Python 分期利息计算法](/interst_rate_calc.py)

##### 例子
>
> [2 万元分 12 期，月还 2266.67，计算链接](https://onlinegdb.com/BkvybphrU)

##### 计算结果
>
> ![银行 12 期分期利息计算结果](/pics/rate_calc_2.png)

### 计算几种情况下的实际利率和还款细节举例
> 可以根据你的 贷款总额、分期数 等信息，计算年化利率
>
>> 1. 您的贷款总额：`Total_money = 20000`
>> 2. 您的总分期数：`Total_month = 12`
>
> 可以根据 类型参数 Type 选择不同的情况计算利息

#### 1. Type = 1：[已知 每期还款现金 和 一次性手续费百分比](https://onlinegdb.com/S1m6AZAr8)
> 1.1 您的每期还款额：`T_1_per_month_money = 2266.67`
>
> 1.2 一次性手续费，单位 %：`T_1_once_rate = 0`

#### 2. Type = 2 ：[已知 月利息 和 每月服务费](https://onlinegdb.com/Bk5C0ZRrI)
> 2.1 每月的利息，单位 %：`T_2_per_month_rate = 0.5`
>
> 2.2 每月的服务费，单位 %：`T_2_per_month_other = 0.1`

#### 3. Type = 3 ：[已知 月利息 和 总服务费](https://onlinegdb.com/HJBV1MRHI)
> 3.1 每月的利息，单位 %： `T_3_per_month_rate = 0.5`
>
> 3.2 服务费总额：`T_3_per_month_other = 2000`

#### 4. Type = 4 ：[已知 日息 和 每月等额，万 3.5 的利息](https://onlinegdb.com/rJg8U1MArU)
> 4.1 每日利息，万分之 3.5：`T_4_per_day_rate = 3.5`

#### 5. Type = 5 ：[已知 日息 和 先息后本，万 3.5 的利息](https://onlinegdb.com/H1pw1GAB8)
> 5.1 每日利息，万分之 3.5：`T_5_per_day_rate = 3.5`


#### 6. Type = 6 ：[已知 每期还款额都不相等，求实际的利息](https://onlinegdb.com/rkzp1MRrU)
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


### 计算几种情况下的存款利息和利率情况

#### 1. Type = 1 ：[已知 存款额、存款期限 和 年化，算利息](https://onlinegdb.com/B1fHQMRrU)
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

#### 2. Type = 2 ：[已知 初期存款、定存周期、定存额度 和 存款期限，算利息](https://onlinegdb.com/SyWImMASU)
> 2.1 首次存款金额：`T_2_first_money = 1000`
>
> 2.2 存款期限，单位年：`T_2_total_years = 5`
>
> 2.3 定存额度：`T_2_per_save = 0`
>
> 2.4 存款间隔，月份：`T_2_time_interval = 12`
>
> 2.5 年化利率：`T_2_year_rate = 3`

#### 3. Type = 3 ：[已知 初期存款、定存周期、定存额度 和 最终总和，算年化利率](https://onlinegdb.com/HyGvmG0SU)
> 3.1 年化利率：`T_3_first_money = 1000`
>
> 3.2 存款期限，单位年：`T_3_total_years = 5`
>
> 3.3 定存额度：`T_3_per_save = 10`
>
> 3.4 存款间隔，月份：`T_3_time_interval = 3`
>
> 3.5 最终本息总和：`T_3_last_total_money = 1376.10`


#### 4. Type = 4 ：[已知 年化利率、定存周期、定存额度 和 最终总和，算最初需要的投入资金](https://onlinegdb.com/BkRD7zRrU)
> 4.1 首次存款金额：`T_4_year_rate = 3`
>
> 4.2 存款期限，单位年：`T_4_total_years = 5`
>
> 4.3 定存额度：`T_4_per_save = 10`
>
> 4.4 存款间隔，月份：`T_4_time_interval = 3`
>
> 4.5 最终本息总和：`T_4_last_total_money = 1376.10`


#### 5. Type = 5 ：[已知 贷款利息、贷款周期、贷款额，算等额本息/等额本金月供](https://onlinegdb.com/Hk9rQMXU8)
> 5.1 年化利率：`T_5_year_rate = 4.66`
>
> 5.2 存款期限，单位年：`T_5_total_years = 20`
>
> 5.3 贷款总额：`T_5_total_money = 434000`

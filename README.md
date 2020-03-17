## 分期真实利率计算器
----

> 很多同学不会算银行的分期真实利率的，这里提供两个方式去帮助你计算银行分期情况下的真实利率。


### 计算不同情况下的真实利率以及还款细节

#### [Type = 1](https://github.com/geekpanshi/rate_calc#1-type--1%E5%B7%B2%E7%9F%A5-%E6%AF%8F%E6%9C%9F%E8%BF%98%E6%AC%BE%E7%8E%B0%E9%87%91-%E5%92%8C-%E4%B8%80%E6%AC%A1%E6%80%A7%E6%89%8B%E7%BB%AD%E8%B4%B9%E7%99%BE%E5%88%86%E6%AF%94) ：已知 每期还款现金 和 一次性手续费百分比
#### [Type = 2](https://github.com/geekpanshi/rate_calc#2-type--2-%E5%B7%B2%E7%9F%A5-%E6%9C%88%E5%88%A9%E6%81%AF-%E5%92%8C-%E6%AF%8F%E6%9C%88%E6%9C%8D%E5%8A%A1%E8%B4%B9) ：已知 月利息       和 每月服务费
#### [Type = 3](https://github.com/geekpanshi/rate_calc#3-type--3-%E5%B7%B2%E7%9F%A5-%E6%9C%88%E5%88%A9%E6%81%AF-%E5%92%8C-%E6%80%BB%E6%9C%8D%E5%8A%A1%E8%B4%B9) ：已知 月利息       和 总服务费
#### [Type = 4](https://github.com/geekpanshi/rate_calc#4-type--4-%E5%B7%B2%E7%9F%A5-%E6%97%A5%E6%81%AF-%E5%92%8C-%E6%AF%8F%E6%9C%88%E7%AD%89%E9%A2%9D%E4%B8%87-35-%E7%9A%84%E5%88%A9%E6%81%AF) ：已知 日息         和 每月等额还款
#### [Type = 5](https://github.com/geekpanshi/rate_calc#5-type--5-%E5%B7%B2%E7%9F%A5-%E6%97%A5%E6%81%AF-%E5%92%8C-%E5%85%88%E6%81%AF%E5%90%8E%E6%9C%AC%E4%B8%87-35-%E7%9A%84%E5%88%A9%E6%81%AF) ：已知 日息         和 先息后本还款
#### [Type = 6](https://github.com/geekpanshi/rate_calc#6-type--6-%E5%B7%B2%E7%9F%A5-%E6%AF%8F%E6%9C%9F%E8%BF%98%E6%AC%BE%E9%A2%9D%E9%83%BD%E4%B8%8D%E7%9B%B8%E7%AD%89%E6%B1%82%E5%AE%9E%E9%99%85%E7%9A%84%E5%88%A9%E6%81%AF) ：已知 每期还款额都不相等，求实际的利息
### 例子说明
> 以借 20000 元，分 12 期，每个月还款 2266.67 元 ，问年化利率是多少？

### 方法一，Excel 12 期分期利息计算法：

#### 计算文件
>
> [银行 12 期分期利息计算表](/银行-12-期分期利息计算表.xlsx)

#### 例子
>
> [2 万元分 12 期，月还 2266.67，计算链接](/银行-12-期分期利息计算表.xlsx)

##### 计算结果
>
> ![银行 12 期分期利息计算表](/pics/rate_calc_1.png)

### 方法二，Python 分期利息计算法（不限分期数目）：

#### 计算源码
>
> [Python 分期利息计算法](/interst_rate_calc.py)

#### 例子
>
> [2 万元分 12 期，月还 2266.67，计算链接](https://onlinegdb.com/BkvybphrU)

##### 计算结果
>
> ![银行 12 期分期利息计算结果](/pics/rate_calc_2.png)

#### Python 脚本其他说明：
> 可以根据你的 贷款总额、分期数 等信息，计算年化利率
>
>> 1. 您的贷款总额：`Total_money = 20000`
>> 2. 您的总分期数：`Total_month = 12`
>
> 可以根据 类型参数 Type 选择不同的情况计算利息

##### 1. Type = 1：[已知 每期还款现金 和 一次性手续费百分比](https://onlinegdb.com/BkvybphrU)
> 1.1 您的每期还款额：`Per_month_money_1 = 2266.67`
>
> 1.2 一次性手续费，单位 %：`Once_rate_1 = 0`

##### 2. Type = 2 ：[已知 月利息 和 每月服务费](https://onlinegdb.com/Hyujf6hBU)
> 2.1 每月的利息，单位 %：`Per_month_rate_2 = 0.5`
>
> 2.2 每月的服务费，单位 %：`Per_month_other_2 = 0.1`

##### 3. Type = 3 ：[已知 月利息 和 总服务费](https://onlinegdb.com/rJ7AzanH8)
> 3.1 每月的利息，单位 %： `Per_month_rate_3 = 0.5`
>
> 3.2 服务费总额：`Per_month_other_3 = 20000`

##### 4. Type = 4 ：[已知 日息 和 每月等额，万 3.5 的利息](https://onlinegdb.com/BkLUc1TBL)
> 4.1 每日利息，万分之 3.5：`Per_day_rate_1 = 3.5`

##### 5. Type = 5 ：[已知 日息 和 先息后本，万 3.5 的利息](https://onlinegdb.com/Sy6PqypSU)
> 5.1 每日利息，万分之 3.5：`Per_day_rate_2 = 3.5`


##### 6. Type = 6 ：[已知 每期还款额都不相等，求实际的利息](https://onlinegdb.com/SyR0gh6S8)
> 6.1 每期还款的按顺序的列表
```python
All_month_pays = [
    67.20,
    84.00,
    86.80,
    105.00,
    108.50,
    108.50,
    105.00,
    108.50,
    105.00,
    108.50,
    108.50,
    10098.00,
]
```

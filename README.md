## 分期真实利率计算器
----

> 很多同学不会算银行的分期真实利率的，这里提供两个方式去帮助你计算银行分期情况下的真实利率。

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
>> 1. 您的贷款总额 Total_money = 20000
>> 2. 您的总分期数 Total_month = 12
>
> 可以根据 类型参数 Type 选择不同的情况计算利息

##### 1. Type = 1：[已知 每期还款现金 和 一次性手续费百分比](https://onlinegdb.com/BkvybphrU)
> 1.1 您的每期还款额
>>
>> Per_month_money_1 = 2266.67
>>
> 1.2 一次性手续费，单位 %
>>
>> Once_rate_1 = 0

##### 2. Type = 2 ：[已知 月利息 和 每月服务费](https://onlinegdb.com/Hyujf6hBU)
> 2.1 每月的利息，单位 %
>>
>> Per_month_rate_2 = 0.5
>
> 2.2 每月的服务费，单位 %
>>
>> Per_month_other_2 = 0.1

##### 3. Type = 3 ：[已知 月利息 和 总服务费](https://onlinegdb.com/rJ7AzanH8)
> 3.1 每月的利息，单位 %
>>
>> Per_month_rate_3 = 0.5
>
> 3.2 服务费总额
>>
>> Per_month_other_3 = 20000

##### 4. Type = 4 ：[已知 日息 和 每月等额，万 3.5 的利息](https://onlinegdb.com/BkLUc1TBL)
> 4.1 每日利息，万分之 3.5，
>>
>> Per_day_rate_1 = 3.5

##### 5. Type = 5 ：[已知 日息 和 先息后本，万 3.5 的利息](https://onlinegdb.com/Sy6PqypSU)
> 5.1 每日利息，万分之 3.5
>>
>> Per_day_rate_2 = 3.5






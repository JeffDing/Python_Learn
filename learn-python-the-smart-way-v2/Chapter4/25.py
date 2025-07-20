'''
Days in Month
题目描述
输入年份和月份，输出这一年的这一月有多少天。需要考虑闰年。

输入格式
输入两个正整数，分别表示年份y 和月数 m，以,隔开。

输出格式
输出一行一个正整数，表示这个月有多少天。

样例输入-1
1926,8
样例输出-1
31
样例输入-2
2000,2
样例输出-2
29

提示
数据保证 
1583≤y≤2020，
1≤m≤12
你可以借鉴Check Leap Year中的闰年判断方法。
'''
import ast
y, m = ast.literal_eval(input())
# 现在程序中有两个变量y, m

# 判断闰年
def is_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

# 确定月份天数
if m in [4, 6, 9, 11]:
    days = 30
elif m == 2:
    if is_leap_year(y):
        days = 29
    else:
        days = 28
else:
    days = 31

print(days)
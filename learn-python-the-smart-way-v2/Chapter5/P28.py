'''
hasConsecutiveDigits
题目描述
给定一个整数n(有可能是正数，也有可能是负数)，你需要判断这个数中是否存在两个相同的连续数字。

输入格式
一个整型数n。

输出格式
一个布尔类型的数，若存在返回True，否则，返回False

输入样例 1
0
输出样例 1
False
输入样例 2
3003
输出样例 2
True
提示说明
在本题中在本题中不要使用字符串索引、字符串方法、列表、列表索引或递归。我们无法技术上强制约束你使用这些特性，请 自觉遵守学术诚信规定。 助教会检查提交的代码，若 不符合本条要求，成绩会被取消。
'''

import ast
n = ast.literal_eval(input())
# 现在程序中有一个变量n

# 在这行注释下面，编写代码，输出你的答案
n = abs(n)  # 处理负数
prev_digit = -1  # 初始化前一位数字
has_consecutive = False

while n > 0:
    current_digit = n % 10
    if current_digit == prev_digit:
        has_consecutive = True
        break
    prev_digit = current_digit
    n = n // 10

print(has_consecutive)
'''
ReverseNumber
题目描述
给定一个自然数n，你需要编写程序，来翻转自然数n。

输入格式
一个整型数n。

输出格式
一个整型数，该数应该是输入数的一个翻转。

输入样例
9870
输出样例
789
提示说明
在本题中不要使用字符串索引、字符串方法、列表、列表索引或递归。我们无法技术上强制约束你使用这些特性，请 自觉遵守学术诚信规定。 助教会检查提交的代码，若 不符合本条要求，成绩会被取消。
有兴趣的同学可以尝试分别使用for、while循环的方式来完成此题。
'''

import ast
n = ast.literal_eval(input())
# 现在程序中有一个变量n

# 在这行注释下面，编写代码，输出你的答案
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10
print(reversed_num)
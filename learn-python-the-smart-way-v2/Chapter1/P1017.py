'''
f-string
题目描述
给定两个整数，按照要求的格式，输出它们之间的乘积。

输入格式
两个整数，用逗号分隔。

输出格式
按照“the product of … and … is: …”的格式输出这两个整数的乘积。

详细情况请参照如下输入/输出样例。

输入样例
3,3
输出样例
the product of 3 and 3 is: 9
'''

import ast
a, b = ast.literal_eval(input())
print(f"the product of {a} and {b} is: {a * b}")
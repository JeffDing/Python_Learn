'''
Is Number
题目描述
我们会为变量 x 赋值，你需要编写程序，判断其是否为数字数据类型，若是返回 True，否则返回 False。

输入格式
Python 数据类型

输出格式
返回 True 或者 False

输入样例-1
100
输出样例-1
True
输入样例-2
'p2s'
输出样例-2
False
提示说明
由于难度问题，我们这里给出程序模板，请 ​在注释说明的部分补全你的代码，如果需要导入模块，请放在代码开头​。

按照课程内容答题，使用暴力枚举将会使你丢失所有分数。
'''

import decimal as numpy
x = eval(input())
# 现在程序中有一个变量 x

print(isinstance(x, (int, float, complex, numpy.Decimal)) and not isinstance(x, bool))
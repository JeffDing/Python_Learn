'''
Is Point Inside Square
题目描述
有一个正方形，四个角的坐标 
(x,y) 分别是 (1,−1)、(1,1)、(−1,−1)、(−1,1)，
x 是横轴，
y 是纵轴。写一个程序，判断一个给定的点是否在这个正方形内（包括正方形边界）。

输入格式
输入一行，包括两个整数 x,y，以一个,分开，表示坐标 (x,y)。

输出格式
输出一行，如果点在正方形内，则输出 True，否则输出 False。

输入样例-1
1,1
输出样例-1
True
'''

import ast
n, m = ast.literal_eval(input())
# 现在程序中有两个变量n, m

# 在这行注释下面，编写代码，输出你的答案
if -1 <= n <= 1 and -1 <= m <= 1:
    print(True)
else:
    print(False)
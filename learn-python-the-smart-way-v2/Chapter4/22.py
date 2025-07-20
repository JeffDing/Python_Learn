'''
getInRange
题目描述
输入3个整数—x，bound1和bound2，其中bound1不一定小于bound2。如果x在两个边界之间，则输出x。否则，如果x小于下限，则输出下限，或者如果x大于上限，则输出上限。

输入格式
输入三个正整数，分别表示x，bounda1和bound2，以,隔开。

输出格式
如果x在两个边界之间，则输出x。否则，如果x小于下限，则输出下限，或者如果x大于上限，则输出上限。

样例输入-1
1,3,5
样例输出-1
3
样例输入-2
4,3,5
样例输出-2
4
'''

import ast
x, bound1, bound2 = ast.literal_eval(input())

# 现在程序中有三个变量 x, bound1, bound2

# 在这行注释下面，编写代码，输出你的答案
lower = min(bound1, bound2)
upper = max(bound1, bound2)

if x < lower:
    print(lower)
elif x > upper:
    print(upper)
else:
    print(x)
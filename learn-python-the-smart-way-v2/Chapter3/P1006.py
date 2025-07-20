'''
circlesIntersect
题目描述
（最后编辑于2023年10月21日）

我们会输入 6 个数字 x1，y1，r1，x2，y2，r2 它们代表两个圆，圆心分别为 (x1, y1) 和 (x2, y2) ，半径分别为 r1 和 r2。你需要编写程序，判断两个圆是否相交，若相交则返回 True ，否则返回 False。（相交指两个圆在一个或多个点接触或重叠）。

输入格式
六个数字，数字类型为整数或者浮点数，以逗号分隔。

输出格式
True 或者 False，判断两个圆是否相交。

输入样例
0,0,2,3,0,2
输出样例
True
'''

import ast
import math

x1, y1, r1, x2, y2, r2 = ast.literal_eval(input())
# 现在程序中有六个变量，x1, y1, r1, x2, y2, r2

# 在这行注释下面，编写代码，输出你的答案
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if distance <= r1 + r2 and distance >= abs(r1 - r2):
    print(True)
else:
    print(False)
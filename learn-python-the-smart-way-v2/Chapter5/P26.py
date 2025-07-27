'''
题目描述
输入正整数n和m，需要编写程序来输出一个n*m的全1矩阵。

输入格式
一个整型数n和一个整型数m，用逗号隔开。

输出格式
输出一个n*m的全1矩阵。

输入样例
2,2
输出样例
1 1
1 1
'''

import ast
n, m = ast.literal_eval(input())
# 现在程序中有两个变量 n, m

# 生成全1矩阵
matrix = [[1 for _ in range(m)] for _ in range(n)]

# 输出矩阵
for row in matrix:
    print(' '.join(map(str, row)))
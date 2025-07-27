'''
题目背景
改编自 洛谷 P1304 哥德巴赫猜想

题目描述
输入一个偶数N，验证4∼N 所有偶数是否符合哥德巴赫猜想：任一大于2 的偶数都可写成两个质数之和。如果一个数不止一种分法，则输出第一个加数相比其他分法最小的方案。例如10=3+7=5+5，则 10=5+5 是要被舍去的答案。

输入格式
第一行输入一个正偶数N

输出格式
输出N−2/2行。对于第i 行：

首先先输出正偶数2i+2，然后输出等号，再输出加和为2i+2 且第一个加数最小的两个质数，以加号隔开。

输入数据 1
10

输出数据 1
4=2+2
6=3+3
8=3+5
10=3+7

提示
数据保证 4≤N≤10000。
'''

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
for num in range(4, n + 1, 2):
    for p in range(2, num // 2 + 1):
        q = num - p
        if is_prime(p) and is_prime(q):
            print(f"{num}={p}+{q}")
            break
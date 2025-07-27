'''
题目背景
改编自 NOIP 2008 提高组 T1

题目描述
小鲸鱼的词汇量很小，所以每次做英语选择题的时候都很头疼。但是它找到了一种方法，经试验证明，用这种方法去选择选项的时候选对的几率非常大！

这种方法的具体描述如下：假设 maxn 是单词中出现次数最多的字母的出现次数，minn 是单词中出现次数最少的字母的出现次数，如果maxn−minn 是一个质数，那么小鲸鱼就认为这是个 Lucky Word，这样的单词很可能就是正确的答案。

输入格式
一个单词，其中只可能出现小写字母，并且长度小于100。

输出格式
共两行，第一行是一个字符串，假设输入的单词被验证是 Lucky Word，那么输出字符串 Lucky Word，否则输出 No Answer；

第二行是一个整数，如果输入单词被验证是 Lucky Word，输出 maxn−minn 的值，否则输出0。

输入数据 1
error
输出数据 1
Lucky Word
2
输入数据 2
olympic
输出数据 2
No Answer
0
提示
【输入输出样例 1 解释】

单词 error 中出现最多的字母r 出现了3 次，出现次数最少的字母出现了1 次，3−1=2，2 是质数。

【输入输出样例 2 解释】

单词 olympic 中出现最多的字母i 出现了1 次，出现次数最少的字母出现了1 次，1−1=0，0 不是质数。
'''
from collections import Counter

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

s = input().strip()
counts = Counter(s)
maxn = max(counts.values())
minn = min(counts.values())
diff = maxn - minn

if is_prime(diff):
    print("Lucky Word")
    print(diff)
else:
    print("No Answer")
    print(0)
'''
Find You
题目描述
输入一串字符串S和一个单词W，要求编写程序，判断单词W是否存在于字符串S当中，并输出响应内容。

输入格式
一串非空字符串S和一个单词W，中间以逗号隔开。

输出格式
详见输入输出样例。

输入样例-1
crazyThurvme50,me
输出样例-1
The starting point of crazyThurvme50 is 11
输入样例-2
crazyThurvme50,KFC
输出样例-2
not found
'''

s, w = input().split(",")
# 现在程序中有两个变量，s和w

# 查找单词在字符串中的位置
position = s.find(w)

if position != -1:
    # 位置从1开始计数
    print(f"The starting point of {s} is {position + 1}")
else:
    print("not found")
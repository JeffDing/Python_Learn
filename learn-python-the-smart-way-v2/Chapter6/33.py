'''
New String
题目描述
输入三串字符串(逗号隔开)str1,str2,str3，要求编写程序，提取每串字符串最末端一个字符，合并组成一个新的字符串并输出。

输入格式
三串非空字符串，中间以逗号空格开。

输出格式
组成后的新字符串。

输入样例-1
APP,222,CS
输出样例-1
P2S
输入样例-2
EFG,MOP,RST
输出样例-2
GPT
'''

str1, str2, str3 = input().split(",")
# 现在程序中有三个字符串，str1,str2,str3

# 提取每个字符串的最后一个字符并合并
new_string = str1[-1] + str2[-1] + str3[-1]

# 输出结果
print(new_string)
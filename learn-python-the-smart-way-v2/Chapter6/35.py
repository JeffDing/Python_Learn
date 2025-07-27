'''
Rotate sentence please
题目描述
输入一串句子(不含标点符号)，单词与单词之间以空格隔开，要求编写程序，将单词顺序进行翻转，但不翻转每个单词的内容。

输入格式
一串非空字符串，包含数个单词，中间以空格隔开，不含标点符号。

输出格式
翻转后的句子。

输入样例
This works but is confusing
输出样例
confusing is but works This
提示说明
提示：本题可以复用翻转字符串部分代码。
'''

str1 = input()
# 现在程序中有一个变量，名为str1

# 分割字符串为单词列表
words = str1.split()

# 反转单词列表
reversed_words = words[::-1]

# 合并反转后的单词为字符串
result = ' '.join(reversed_words)

# 输出结果
print(result)
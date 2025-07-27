'''
Upper and Lower
题目描述
输入一串字符串str1，要求编写程序，将其中所有的大写字母和小写字母进行转换，输出转换后字符串。

输入格式
一串非空字符串str1，只包含大小写字母元素。

输出格式
一串转换后的字符串。

输入样例
abcdEFG
输出样例
ABCDefg
提示说明
注意大写字母指代A~Z，小写字母指代a~z。
'''

str1 = input()
# 现在程序中有一个字符串，str1

# 初始化一个空字符串用于存储转换后的结果
result = ""

# 遍历字符串中的每个字符
for char in str1:
    if char.isupper():
        # 如果是大写字母，转换为小写
        result += char.lower()
    elif char.islower():
        # 如果是小写字母，转换为大写
        result += char.upper()
    else:
        # 其他字符保持不变（虽然题目说明只有字母）
        result += char

# 输出结果
print(result)
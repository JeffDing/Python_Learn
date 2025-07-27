'''
isPalindrome
题目描述
输入三串字符串(逗号隔开)str1,str2,str3，要求编写程序，判断这些字符串是否为回文字符串，如果是则输出T，否则输出F。

输入格式
三串非空字符串，中间以逗号空格开。

输出格式
输出T或者F，中间以逗号空格开。

输入样例-1
abc,bbb,abcdcba
输出样例-1
F,T,T
输入样例-2
111,yyds,dddd
输出样例-2
T,F,T
'''

str1, str2, str3 = input().split(",")
# 现在程序中有三个字符串，str1,str2,str3

# 定义回文判断函数
def is_palindrome(s):
    return s == s[::-1]

# 判断三个字符串是否为回文
result1 = 'T' if is_palindrome(str1) else 'F'
result2 = 'T' if is_palindrome(str2) else 'F'
result3 = 'T' if is_palindrome(str3) else 'F'

# 输出结果
print(f"{result1},{result2},{result3}")
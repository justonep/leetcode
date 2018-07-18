# -*- coding: utf-8 -*-
def first_char(str):
    str=str.lower()
    dict1 = {}
    for i in range(len(str)):
        #累计字符的出现次数
        if str[i] in dict1:
            dict1[str[i]] += 1
        #只出现一次，key对应的value就记1次
        else:
            dict1[str[i]] = 1
    for i in range(len(str)):
        if dict1[str[i]] == 1:
            return str[i], i+1

if __name__ == '__main__':
    str1 = 'aaABb2dDEEFKKR'
    print(first_char(str1))
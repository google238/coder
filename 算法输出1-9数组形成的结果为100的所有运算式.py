# -*- coding: utf-8 -*-
operator = {
 1: '+',
 2: '-',
 0: ''
}
base = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def isHundred(num):
    #转化为8位3进制数，得到运算符数组
    arr = []
    for index in range(8):
        index = 7 - index
        arr.append(num // (3 ** index))
        num -= (num // (3 ** index)) * (3 ** index)
        print num
    arr = map(lambda x: operator[x], arr)
    #合并得到运算式
    formula = reduce(lambda x, y: x + y, zip(base, arr))
    formula = list(formula)
    formula.append('9')
    formula = ''.join(formula)
    #计算运算式结果
    res = eval(formula)
    return res, formula


if __name__ == '__main__':
    #所有可能的结果
    total = 3 ** 8
    for i in range(total):
        res, formula = isHundred(i)
        if res == 100:
            print (formula+' = 100')
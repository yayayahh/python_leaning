# -*- coding:utf-8 -*-
# __author : huangrongya
# @Desc : ================================================
# Life is short I use Python!!!                        ===
# If this runs wrong,don't ask me,I don't know why...  ===
# If this runs right,thank god,and I don't know why... ===
# Maybe the answer,my friend,is blowing in the wind... ===
# ========================================================
# date : 2018/6/6 0006 10:50
# @Project : python_leaning
# @FileName: demo_1.py

s = (x * 2 for x in range(5))

for i in s:
    print(i)


def func():
    print('hello python')
    yield


# print(func())
for i in func():
    print(i)

g=func()
print(next(g))

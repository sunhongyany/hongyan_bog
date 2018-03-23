Title: 切片
Date: 2017-06-24 20:30
Category: 学习笔记
Tags: python

给切片赋值

    >>> l = list(range(10))
    >>> l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> l[2:5] = ['a']
    >>> l
    [0, 1, 'a', 5, 6, 7, 8, 9]
    >>> l[3:6:2] = ['b', 'c']
    >>> l
    [0, 1, 'a', 'b', 6, 'c', 8, 9]

但是赋值对象是切片时，赋值语句右面必须是个可迭代对象。

    >>> l[3:5] = 3
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only assign an iterable
    >>> l[3:5] = [3]
    >>> l
    [0, 1, 'a', 3, 'c', 8, 9]

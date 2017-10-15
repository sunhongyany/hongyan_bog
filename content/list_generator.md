Title: python中的内置序列（二）
Date: 2010-06-03 20:20
Category: python

列表推导式python2与python3区别

在python2中：

    >>> [x for x in range(5)]
    [0, 1, 2, 3, 4]
    >>> x
    4
    >>> i = 0
    >>> [i for i in range(5)]
    [0, 1, 2, 3, 4]
    >>> i
    4


在python3中：

    >>> [x for x in range(5)]
    [0, 1, 2, 3, 4]
    >>> x
    Traceback (most recent call last):
        File "<pyshell#2>", line 1, in <module>
            x
    NameError: name 'x' is not defined
    >>> i = 1
    >>> [i for i in range(5)]
    [0, 1, 2, 3, 4]
    >>> i
    1

在python3中列表推导式，生成器表达式，以及集合推导，字典推导都有了自己的局部作用域。

filter和map合起来能做的事，列表推导式也可以。

    >>> s = 'asdf'
    >>> l = [ord(i) for i in s if ord(i)>100]
    >>> l
    [115, 102]
    >>> f = list(filter(lambda x: x>100, map(ord, s)))
    >>> f
    [115, 102]

在python2中filter和map返回列表，在python3下则分别返回filter对象和map对象。

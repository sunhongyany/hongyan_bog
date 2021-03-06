Title: python中的内置序列（二）
Date: 2017-06-03 22:20
Category: 学习笔记
Tags: python

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

如果一个生成器表达式是一个函数调用的唯一参数，那么不需要在用额外的括号把他们围起来。

    >>> s = 'asdf'
    >>> list(ord(i) for i in s)
    >>>[97, 115, 100, 102]
    >>>import array
    >>> array.array('I',(ord(i) for i in s))
    array('I', [97, 115, 100, 102])
    >>> array.array('I',ord(i) for i in s)
    SyntaxError: Generator expression must be parenthesized if not sole argument

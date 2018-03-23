Title: 序列增量赋值
Date: 2017-06-24 20:30
Category: 学习笔记
Tags: python

&emsp;&emsp;+=背后的特殊方法是__iadd__(用于就地加法)，如果一个类没有这个方法，就会调用__add__。

a += b如果a没有实现__iadd__方法，a += b 就和a = a + b一样。*=和+=用法一样。

```python

    In [19]: l1 = [1, 2, 3, 4]

    In [20]: id(l1)
    Out[20]: 4537296648

    In [21]: l1 += [0]

    In [22]: l1
    Out[22]: [1, 2, 3, 4, 0]

    In [25]: id(l1)
    Out[25]: 4537296648

    In [23]: l2 = (1, 2, 3, 4)

    In [24]: id(l2)
    Out[24]: 4537142312

    In [27]: l2 += (0,)

    In [29]: l2
    Out[29]: (1, 2, 3, 4, 0)

    In [30]: id(l2)
    Out[30]: 4536380232

```

&emsp;&emsp;对不可变的序列进行重复拼接操作的话效率会很低，因为每次都有个新的对象，python解释器都会

把需要把原来的对象中的元素先复制到新的对象里,然后再追加新的元素。但是str是一个例外,cpython

对其做了优化，为str初始化内存时，程序为他留出可扩展空间，因此进行增量操作时，并不会涉及复制

原有字符串到新位置这类操作。

一个奇怪的现象：

```python

    In [31]: l = (1, 2, [3, 4])

    In [32]: l[2] += [5, 6]
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-32-d67deada9dc4> in <module>()
    ----> 1 l[2] += [5, 6]

    TypeError: 'tuple' object does not support item assignment

    In [33]: l
    Out[33]: (1, 2, [3, 4, 5, 6])

```

在python3.6和python2.7都这样。

title: __all__的作用
Date: 2017-06-24 20:30
Category: 学习笔记
tags: python

__all__是一个string元素组成的list变量，定义了当你使用 from <module> import * 导入某个模块的时候能导出的符

号（这里代表变量，函数，类等）。

举个例子，在all_test.py中，我们明确导出符号a，b。

```python
    1   __all__ = ['a', 'b']
      1
      2 a = 1
      3 b = 2
      4 c = 3
```

在ipython中我们输入：

```python
    In [1]: from all_test import *

    In [2]: print(a)
    1

    In [3]: print(b)
    2

    In [4]: print(c)
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-4-1dd5973cae19> in <module>()
    ----> 1 print(c)

    NameError: name 'c' is not defined
```

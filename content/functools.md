title: functools.lru_cache
Date: 2017-06-25 20:30
Category: python

functools.lru_cache实现了备忘功能，他把耗时的函数结果保存起来，避免传入相同的参数时重复计

算。

斐波拉契数列很耗时，此时用functools.lru_cache最好。

首先定义一个计时器。然后计算没有用functools.lru_cache的用时的耗时，最后计算用了

functools.lru_cache的耗时。

```python 
In [77]: import time

In [78]: import functools

In [79]: def timer(func):
    ...:     @functools.wraps(func)
    ...:     def clock(*args, **kwargs):
    ...:         t0 = time.perf_counter()
    ...:         result = func(*args, **kwargs)
    ...:         elapsed = time.perf_counter() - t0
    ...:         if args:
    ...:             arg_str = ','.join(repr(arg) for arg in args)
    ...:         else:
    ...:             arg_list = ['%s=%r'%(key, val)for key, val in sorted(kwargs.items())]
    ...:             arg_str = ','.join(repr(arg) for arg in arg_list)
    ...:         print('[%0.8fs] %s(%s) -> %r'%(elapsed, func.__name__, arg_str, result))
    ...:         return result
    ...:     return clock
    ...:

In [80]: @timer
    ...: def fibonacci(n):
    ...:     if n<2:
    ...:         return n
    ...:     else:
    ...:         return fibonacci(n-2) + fibonacci(n-1)
    ...:

In [81]: fibonacci(5)
[0.00000057s] fibonacci(1) -> 1
[0.00000083s] fibonacci(0) -> 0
[0.00000080s] fibonacci(1) -> 1
[0.00004263s] fibonacci(2) -> 1
[0.00013928s] fibonacci(3) -> 2
[0.00000069s] fibonacci(0) -> 0
[0.00000093s] fibonacci(1) -> 1
[0.00003494s] fibonacci(2) -> 1
[0.00000070s] fibonacci(1) -> 1
[0.00000081s] fibonacci(0) -> 0
[0.00000088s] fibonacci(1) -> 1
[0.00003424s] fibonacci(2) -> 1
[0.00006857s] fibonacci(3) -> 2
[0.00013949s] fibonacci(4) -> 3
[0.00031221s] fibonacci(5) -> 5
Out[81]: 5

In [82]: @functools.lru_cache()
    ...: @timer
    ...: def fibonacci(n):
    ...:     if n<2:
    ...:         return n
    ...:     else:
    ...:         return fibonacci(n-2) + fibonacci(n-1)
    ...:

In [83]: fibonacci(6)
[0.00000048s] fibonacci(0) -> 0
[0.00000066s] fibonacci(1) -> 1
[0.00003910s] fibonacci(2) -> 1
[0.00000111s] fibonacci(3) -> 2
[0.00005868s] fibonacci(4) -> 3
[0.00000083s] fibonacci(5) -> 5
[0.00007846s] fibonacci(6) -> 8
Out[83]: 8
```

可以看出利用了functools.lru_cache调用次数变少，因为他把调用过的结果都保存了起来。

lru_cache有两个可选的参数，他的签名是：functools.lru_cache(maxsize=128, typed=false)

maxsize指定缓存多少个调用结果, 缓存满了之后，旧的值会被扔掉，腾出空间，为了得到最佳性能，

maxsize应设为2的幂。typed被设为true，把不同的参数类型得到的结果分开保存，即认为相等的1和

1.0区分开。lru_cache使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，所

以被lru_cache装饰的函数，它的所有参数都是可散列的。

假设我们要生成调试web 应用的工具，我们想生成THML，显示不同类型的python对象。

可以定义如下函数：

```python
In [86]: import html

In [87]: def htmlize(obj):
    ...:     content = html.escape(repr(obj))
    ...:     return '<pre>{}</pre>'.format(content)
    ...:
```

这个程序适用于任何python类型，但是现在要求以特别的方式显示某些类型。

str：把内部的换行符替换为``` '<br>\n'; ```不使用```<pre> ```,使用``` <p> ```。

int：以十进制和十六进制显示数字。

list：输出一个html列表，根据各个元素的类型进行格式化。

python不支持重载方法和函数，所以我们不能使用不同的签名来定义html变体，也无法使用不同的方式处

理不同的数据类型，在python中一种常见的做法是把html变成一个分派函数，使用一串if／elif调用专门

的函数，这样不便于用户模块的扩展，还显得笨拙，时间一长，分派函数htmlize会变得很大，而且会与各

个专门函数之间的耦合很紧密。

functools.singledispatch装饰器可以把整体方案拆分成多个模块，甚至可以为你无法修改的函数提供专门

的函数。使用@singledispatch装饰的普通函数会变成泛函数。

```python
In [89]: from functools import singledispatch

In [90]: from collections import abc

In [91]: import numbers

In [92]: import html

In [93]: @singledispatch
    ...: def htmlize(obj):
    ...:     content = html.escape(repr(obj))
    ...:     return '<pre>{}<pre>'.format(content)
    ...:

In [94]: @htmlize.register(str)
    ...: def _(text):
    ...:     content = html.escape(text).replace('\n', '<br>\n')
    ...:     return '<p>{}</p>'.format(content)
    ...:

In [95]: @htmlize.register(numbers.Integral)
    ...: def _(n):
    ...:     return '<pre>{0} (0x{0: x})</pre>'.format(n)
    ...:

In [96]: @htmlize.register(tuple)
    ...: @htmlize.register(abc.MutableSequence)
    ...: def _(seq):
    ...:     inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    ...:     return '<ul>\n<li>' + inner + '</li>\n</ul>'

In [99]: htmlize({1, 2, 3})
Out[99]: '<pre>{1, 2, 3}<pre>'

In [102]: htmlize(12)
Out[102]: '<pre>12 (0xc)</pre>'

In [103]: htmlize(['q', 12, {1, 2, 3}])
Out[103]: '<ul>\n<li><p>q</p></li>\n<li><pre>12 (0xc)</pre></li>\n<li><pre>{1, 2, 3}
<pre></li>\n</ul>'
```


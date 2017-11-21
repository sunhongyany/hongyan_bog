title: 装饰器
Date: 2017-06-25 20:30
Category: python

函数装饰器用于在源码中标记函数，以某种方式增强函数的行为。

装饰器的特性：

    1. 能把被装饰的函数替换成其他函数。

    2. 装饰器在加载模块时立即执行。

实现一个简单的装饰器。它会在每次调用被装饰的函数时计时，然后把经过的时间，传入的参数，调用

的结果打印出来.

```python
In [39]: import time

In [44]: def timer(func):
    ...:     def clock(*args):
    ...:         t0 = time.perf_counter()
    ...:         result = func(*args)
    ...:         elapsed = time.perf_counter() - t0
    ...:         arg_str = ','.join(repr(arg) for arg in args)
    ...:         print('[%0.8fs] %s(%s) -> %r'%(elapsed, func.__name__, arg_str, result))
    ...:         return result
    ...:     return clock
    ...:

In [45]: @timer
    ...: def factorial(n):
    ...:     return 1 if n<2 else n * factorial(n-1)
    ...:
    ...:

In [46]: factorial(5)
[0.00000072s] factorial(1) -> 1
[0.00004617s] factorial(2) -> 2
[0.00006397s] factorial(3) -> 6
[0.00007730s] factorial(4) -> 24
[0.00009103s] factorial(5) -> 120
Out[46]: 120
```

timer装饰器有几个缺点：不支持关键字参数，而且遮盖了被装饰函数的__name__属性和__doc__属性。

functools.wrap装饰器把相关的属性从func复制到clock中。

```python
In [57]: import functools

In [58]: import time

In [59]: def timer(func):
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

In [60]: @timer
    ...: def kw_func(k=1):
    ...:     print(k)
    ...:

In [61]: kw_func(k=2)
2
[0.00002102s] kw_func('k=2') -> None

In [62]: @timer
    ...: def kw_func(k=1):
    ...:     return k
    ...:

In [63]: kw_func(k=2)
[0.00000107s] kw_func('k=2') -> 2
Out[63]: 2
```
